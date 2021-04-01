from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from ..models import Todo
from ..serializers import TodoSerializer


class TodoListAndCreate(APITestCase):
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
