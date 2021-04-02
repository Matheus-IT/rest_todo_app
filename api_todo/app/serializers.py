from app.models import Task
from rest_framework.serializers import ModelSerializer

class TaskSerializer(ModelSerializer):
	class Meta:
		model = Task
		fields = ['id', 'name', 'done', 'created_at']
