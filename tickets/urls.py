from django.urls import path 
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.home, name='home'),
    path('ticket/<uuid:uuid>/', views.details, name='detail'),
    path('ticket/new/', views.new_ticket, name='new')
]