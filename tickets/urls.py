from django.urls import path 

from . import views


app_name = 'tickets'

urlpatterns = [
    # /
    path('',                          views.get_started,   name='get-started'),
    
    # /ticket/
    path('ticket/<uuid:uuid>/delete', views.delete_ticket, name='delete'),
    path('ticket/',                   views.home,          name='home'),
    path('ticket/<uuid:uuid>/',       views.details,       name='detail'),
    path('ticket/new/',               views.new_ticket,    name='new'),
    path('ticket/<uuid:uuid>/edit/',  views.edit_ticket,   name='edit'),
    path('ticket/search/',            views.search_ticket, name='search'),
    path('ticket/<uuid:uuid>/reply/', views.reply_ticket,  name='reply')
]