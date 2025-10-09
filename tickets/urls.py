from django.urls import path 

from . import views

""" App namespace """
app_name = 'tickets'

""" All URls and Views """
urlpatterns = [
    # / 
    path('',                           views.get_started,   name='get-started'),
    # /ticket/
    path('ticket/',                    views.home,          name='home'),
    path('ticket/new/',                views.new_ticket,    name='new'),
    path('ticket/search/',             views.search_ticket, name='search'),
    path('ticket/<uuid:uuid>/',        views.details,       name='detail'),
    path('ticket/<uuid:uuid>/edit/',   views.edit_ticket,   name='edit'),
    path('ticket/<uuid:uuid>/delete/', views.delete_ticket, name='delete'),
    path('ticket/<uuid:uuid>/reply/',  views.reply_ticket,  name='reply')
]