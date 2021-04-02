from rest_framework import status, generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


class TodoListAndCreate(generics.ListCreateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
