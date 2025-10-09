from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
from django import shortcuts


""" Creates the Category Model """
class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


""" Creates the Priority Model """
class Priority(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


""" Creates the Status Model """
class Status(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


""" Creates the TicketManager Manager """
class TicketManager(models.Manager):
    def get_by_uuid_or_404(self, uuid):
        return shortcuts.get_object_or_404(self.model, uuid=uuid)


""" Creates the Ticket Model """
class Ticket(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=200)
    solution = models.TextField(default='', blank=True)
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        default=1
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        null=True,
        default=1
    )
    status = models.ForeignKey(
        Status, 
        on_delete=models.SET_NULL, 
        null=True, 
        default=1
    )
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = TicketManager()
    
    def __str__(self):
        return self.title
    