from django import forms

from .models import Ticket


class TicketCreateForm(forms.ModelForm):
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
    

class TicketEditForm(forms.ModelForm):
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
        
        
class SearchTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title'
        ]


class ReplyTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'solution'
        ]