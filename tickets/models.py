from uuid import uuid4

from django.db.models import (
    Model,
    CharField,
    Manager,
    UUIDField,
    ForeignKey,
    SET_NULL,
    TextField,
    CASCADE,
    DateTimeField
)
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


""" Creates the Category Model """
class Category(Model):
    name = CharField(max_length=40)

    def __str__(self):
        return self.name


""" Creates the Priority Model """
class Priority(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


""" Creates the Status Model """
class Status(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


""" Creates the TicketManager Manager """
class TicketManager(Manager):
    def get_by_uuid_or_404(self, uuid):
        return get_object_or_404(self.model, uuid=uuid)


""" Creates the Ticket Model """
class Ticket(Model):
    uuid = UUIDField(default=uuid4, editable=False, unique=True)

    title = CharField(max_length=65)
    description = CharField(max_length=200)
    solution = TextField(default='', blank=True)

    category = ForeignKey(
        Category,
        on_delete=SET_NULL,
        null=True,
        default=1
    )
    priority = ForeignKey(
        Priority,
        on_delete=SET_NULL,
        null=True,
        default=1
    )
    status = ForeignKey(
        Status,
        on_delete=SET_NULL,
        null=True,
        default=1
    )
    created_by = ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=CASCADE
    )

    creation_date = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    objects = TicketManager()

    def __str__(self):
        return self.title
