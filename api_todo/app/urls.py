from django.urls import path

from .views import TodoListAndCreate, TodoDetailChangeAndDelete


urlpatterns = [
	path('', TodoListAndCreate.as_view(), name='tasks-list'),
	path('<int:pk>/', TodoDetailChangeAndDelete.as_view(), name='tasks-detail'),
]
