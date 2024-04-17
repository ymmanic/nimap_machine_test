from rest_framework import serializers
from .models import Client, Project

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name', read_only=True)
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_name', 'users', 'created_at', 'created_by']
