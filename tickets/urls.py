from django.urls import path

from .views import (
    get_started,
    home,
    new_ticket,
    search_ticket,
    details,
    edit_ticket,
    delete_ticket,
    reply_ticket,
)


""" App namespace """
app_name = 'tickets'

""" All URls and Views """
urlpatterns = [
    # /
    path('',                           get_started,   name='get-started'),
    # /ticket/
    path('ticket/',                    home,          name='home'),
    path('ticket/new/',                new_ticket,    name='new'),
    path('ticket/search/',             search_ticket, name='search'),
    path('ticket/<uuid:uuid>/',        details,       name='detail'),
    path('ticket/<uuid:uuid>/edit/',   edit_ticket,   name='edit'),
    path('ticket/<uuid:uuid>/delete/', delete_ticket, name='delete'),
    path('ticket/<uuid:uuid>/reply/',  reply_ticket,  name='reply'),
]
