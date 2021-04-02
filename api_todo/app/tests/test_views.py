from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from ..models import Todo
from ..serializers import TodoSerializer


class TodoListAndCreateTests(APITestCase):
	def setUp(self):
		self.AMOUNT_CREATED = 5

		for i in range(self.AMOUNT_CREATED):
			Todo.objects.create(
				name=f'{i}Task for tests'
			)
	
	def test_get_tasks_list(self):
		response = self.client.get(reverse('tasks-list'))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), self.AMOUNT_CREATED)

	def test_post_new_task(self):
		data = {
			'name': 'Simple task to test post request'
		}
		response = self.client.post(reverse('tasks-list'), data=data)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data['name'], data['name'])
	
	def test_post_new_invalid_task(self):
		""" Sending invalid data """
		data = {}
		response = self.client.post(reverse('tasks-list'), data=data)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TodoDetailChangeAndDeleteTests(APITestCase):
	def setUp(self):
		self.AMOUNT_CREATED = 2

		for i in range(self.AMOUNT_CREATED):
			Todo.objects.create(
				name=f'{i}Task for tests'
			)
	
	def test_get_single_task(self):
		response = self.client.get(reverse('tasks-detail', kwargs={'pk': 1}))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_get_invalid_task(self):
		""" Requesting a task that doesn't exist """
		response = self.client.get(reverse('tasks-detail', kwargs={'pk': 999}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_put_updating_task(self):
		data = {
			'name': 'This is a new name for testing purposes'
		}
		response = self.client.put(reverse('tasks-detail', kwargs={'pk': 1}), data=data)
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['name'], data['name'])

	def test_put_updating_invalid_task(self):
		""" Updating data of nonexisting task """
		data = {
			'name': 'This is a new name for testing purposes'
		}
		response = self.client.put(reverse('tasks-detail', kwargs={'pk': 999}), data=data)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
	
	def test_put_updating_invalid_data(self):
		""" Test updating bad request """
		data = {}
		response = self.client.put(reverse('tasks-detail', kwargs={'pk': 1}), data=data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
	
	def test_delete_task(self):
		response = self.client.delete(reverse('tasks-detail', kwargs={'pk': 1}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
	
	def test_delete_nonexisting_task(self):
		response = self.client.delete(reverse('tasks-detail', kwargs={'pk': 999}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
