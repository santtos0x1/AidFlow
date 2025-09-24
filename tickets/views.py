from django.contrib import messages
from django import shortcuts

from . import models
from . import forms

""" Renders the Get-Started """
def get_started(request):
    return shortcuts.render(
        request,
        'tickets/pages/get-started.html'
    )

""" Renders the Home with the context """
def home(request):
    query_set_id = shortcuts.get_list_or_404(models.Ticket)
    
    return shortcuts.render(
        request,
        'tickets/pages/home.html', 
        {
            'tickets' : query_set_id
        }
    )

""" Renders the Details with the context """
def details(request, uuid):
    ticket = models.Ticket.objects.get_by_uuid_or_404(uuid=uuid)
    
    return shortcuts.render(
        request,
        'tickets/pages/detail.html', 
        {
            'ticket': ticket
        }
    )


""" Deletes the tickert and redirects to the home page """
def delete_ticket(request, uuid):
    ticket = models.Ticket.objects.get_by_uuid_or_404(uuid=uuid)
    
    if request.method == 'POST' and request.POST.get('action') == 'delete_confirm':
        ticket.delete()
        messages.success(
            request,
            'Ticket deleted successfully.'
        )
        return shortcuts.redirect('tickets:home')
    
    return shortcuts.render(
        request,
        'tickets/pages/detail.html', 
        {
            'ticket': ticket
        }
    )
    
""" Reply the ticket and redirects to the details page """
def reply_ticket(request, uuid):
    ticket = models.Ticket.objects.get_by_uuid_or_404(uuid=uuid)
    form = forms.ReplyTicketForm(request.POST, instance=ticket)
    
    if request.method == 'POST' and form.is_valid():
        form_ticket = form.save(commit=False)
        form_ticket.created_by = request.user
        form.save()
        return shortcuts.redirect('tickets:detail', uuid=ticket.uuid)
    else:
        form = forms.ReplyTicketForm(instance=ticket)
            
    return shortcuts.render(
        request, 
        'tickets/pages/reply-page.html',
        {
            'ticket': ticket,
            'form': form
        }
    )

""" Edit the ticket and redirects to the home page """
def edit_ticket(request, uuid):
    ticket = models.Ticket.objects.get_by_uuid_or_404(uuid=uuid)
    form = forms.TicketEditForm(request.POST, instance=ticket)
    
    if request.method == 'POST' and form.is_valid():
        form_ticket = form.save(commit=False)
        form_ticket.created_by = request.user 
        form.save()
        return shortcuts.redirect('tickets:home')
    else:
        form = forms.TicketEditForm(instance=ticket)
            
    return shortcuts.render(
        request,
        'tickets/pages/edit-ticket.html',
        {
            'ticket': ticket,
            'form': form
        }
    )
    
""" Creates a new ticket and redirects to the home page """
def new_ticket(request):
    form = forms.TicketCreateForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form_ticket = form.save(commit=False)
        form_ticket.created_by = request.user 
        form.save()
        return shortcuts.redirect('tickets:home')
    else:
        form = forms.TicketCreateForm()
        
    return shortcuts.render(
        request,
        'tickets/pages/new-ticket.html', 
        {
            'form': form
        }
    )

""" Searchs the ticket with the query """
def search_ticket(request):
    query = request.GET.get('q', '')
    
    if query:
        tickets = models.Ticket.objects.filter(title__icontains=query)
    else:
        tickets = models.Ticket.objects.all()
        
    return shortcuts.render(
        request,
        'tickets/pages/search.html', 
        {
            'tickets': tickets
        }
    )
    