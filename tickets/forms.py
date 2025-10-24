from django.forms import ModelForm

from .models import Ticket


""" Creates the Ticket-Create Form """
class TicketCreateForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'category',
            'priority'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = ""
        self.fields['priority'].empty_label = ""


""" Creates the Ticket-Edit Form """
class TicketEditForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'category',
            'priority',
            'status'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = ""
        self.fields['priority'].empty_label = ""


""" Creates the Search-Ticket Form """
class SearchTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title'
        ]


""" Creates the Reply-Ticket Form """
class ReplyTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'solution'
        ]