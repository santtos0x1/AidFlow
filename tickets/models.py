from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Ticket(models.Model):
    # Identification
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # Basic Information
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=200)
    solution = models.TextField(default='', blank=True)
    
    # Relationships
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(
        Status, 
        on_delete=models.SET_NULL, 
        null=True, 
        default=1
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Timestamps
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title