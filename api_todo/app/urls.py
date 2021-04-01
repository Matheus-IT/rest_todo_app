from django.urls import path

from .views import TodoListAndCreate, todo_detail_change_and_delete


urlpatterns = [
	path('', TodoListAndCreate.as_view(), name='tasks-list'),
	path('<int:pk>/', todo_detail_change_and_delete, name='tasks-detail'),
]
