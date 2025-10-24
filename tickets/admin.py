from django.contrib.admin import ModelAdmin, register

from .models import Ticket, Category, Status, Priority


""" Register Ticket on /admin/ """
@register(Ticket)
class TicketAdmin(ModelAdmin):
    pass


""" Register Category on /admin/ """
@register(Category)
class CategoryAdmin(ModelAdmin):
    pass


""" Register Status on /admin/ """
@register(Status)
class StatusAdmin(ModelAdmin):
    pass


""" Register Priority on /admin/ """
@register(Priority)
class PriorityAdmin(ModelAdmin):
    pass
