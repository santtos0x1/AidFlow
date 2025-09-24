from django.contrib import admin

from . import models

""" Register Ticket on /admin/ """
@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
    
""" Register Category on /admin/ """
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    
""" Register Status on /admin/ """
@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    pass
    
""" Register Priority on /admin/ """
@admin.register(models.Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass
