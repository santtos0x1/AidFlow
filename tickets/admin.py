from django.contrib.admin import ModelAdmin, register

from .models import Ticket, Category, Status, Priority


# Register Ticket on /admin/
@register(Ticket)
class TicketAdmin(ModelAdmin):
    """Admin configuration for Ticket."""
    pass


# Register Category on /admin/
@register(Category)
class CategoryAdmin(ModelAdmin):
    """Admin configuration for Category."""
    pass


# Register Status on /admin/
@register(Status)
class StatusAdmin(ModelAdmin):
    """Admin configuration for Status."""
    pass


# Register Priority on /admin/
@register(Priority)
class PriorityAdmin(ModelAdmin):
    """Admin configuration for Priority."""
    pass
