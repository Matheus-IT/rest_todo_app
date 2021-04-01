from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
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


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_change_and_delete(request, pk):
	try:
		todo = Todo.objects.get(pk=pk)
	except Todo.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serialized = TodoSerializer(todo)
		return Response(serialized.data)
	elif request.method == 'PUT':
		serialized = TodoSerializer(todo, data=request.data)
		
		if serialized.is_valid():
			serialized.save()
			return Response(serialized.data)
		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
