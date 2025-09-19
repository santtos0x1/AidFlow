from django.contrib import admin
from .models import Ticket, Status, Priority, Category

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    ...