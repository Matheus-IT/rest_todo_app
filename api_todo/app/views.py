from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer


class TodoListAndCreate(APIView):
	def get(self, request):
		todo = Todo.objects.all()
		serialized = TodoSerializer(todo, many=True)
		return Response(serialized.data)
	
	def post(self, request):
		serialized = TodoSerializer(data=request.data)

		if serialized.is_valid():
			serialized.save()
			return Response(serialized.data, status=status.HTTP_201_CREATED)
		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailChangeAndDelete(APIView):
	def get_object(self, pk):
		try:
			return Todo.objects.get(pk=pk)
		except Todo.DoesNotExist:
			raise NotFound()

	def get(self, request, pk):
		todo = self.get_object(pk)
		serialized = TodoSerializer(todo)
		return Response(serialized.data)

	def put(self, request, pk):
		todo = self.get_object(pk)
		serialized = TodoSerializer(todo, data=request.data)

		if serialized.is_valid():
			serialized.save()
			return Response(serialized.data)
		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk):
		todo = self.get_object(pk)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
