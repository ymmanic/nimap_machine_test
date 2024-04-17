from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_clients')

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects_assigned')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')

