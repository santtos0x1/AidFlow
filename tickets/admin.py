from django.contrib import admin

from . import models


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
    
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    
    
@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    pass
    
    
@admin.register(models.Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass
