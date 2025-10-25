from django.contrib.messages import success, error
from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Ticket
from .forms import ReplyTicketForm, TicketEditForm, TicketCreateForm


""" Returns the Ticket model retrieved by uuid or 404 """
def get_ticket_by_uuid_or_404(uuid):
    ticket = Ticket.objects.get_by_uuid_or_404(uuid=uuid)

    return ticket

""" Renders the Get-Started """
def get_started(request):
    return render(
        request,
        'tickets/pages/get-started.html'
    )

""" Renders the Home with the context """
def home(request):
    tickets = Ticket.objects.all()

    return render(
        request,
        'tickets/pages/home.html',
        {
            'tickets' : tickets
        }
    )

""" Renders the Details with the context """
def details(request, uuid):
    ticket = get_ticket_by_uuid_or_404(uuid=uuid)

    return render(
        request,
        'tickets/pages/detail.html',
        {
            'ticket': ticket
        }
    )

""" Deletes the tickert and redirects to the home page """
def delete_ticket(request, uuid):
    ticket = get_ticket_by_uuid_or_404(uuid=uuid)

    if request.method == 'POST' and request.POST.get('action') == 'delete_confirm':
        ticket.delete()
        success(request, 'Ticket deleted successfully.')
        return redirect('tickets:home')

    error(
        request,
        'Error on ticket delete, ticket not deleted.'
    )
    return render(
        request,
        'tickets/pages/detail.html',
        {
            'ticket': ticket
        }
    )

""" Reply the ticket and redirects to the details page """
def reply_ticket(request, uuid):
    ticket = get_ticket_by_uuid_or_404(uuid=uuid)

    if request.method == 'POST':
        form = ReplyTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            success(request, 'Ticket replied sucessfully.')
            return redirect('tickets:detail', uuid=ticket.uuid)
        else:
            error(request, 'Error: invalid form data.')
    else:
        form = ReplyTicketForm(instance=ticket)

    return render(
        request,
        'tickets/pages/reply-page.html',
        {
            'ticket': ticket,
            'form': form
        }
    )

""" Edit the ticket and redirects to the home page """
def edit_ticket(request, uuid):
    ticket = get_ticket_by_uuid_or_404(uuid=uuid)

    if request.method == 'POST':
        form = TicketEditForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            success(request, 'Ticket edited sucessfully.')
            return redirect('tickets:home')
        else:
            error(request, 'Error: invalid form data.')
    else:
        form = TicketEditForm(instance=ticket)

    return render(
        request,
        'tickets/pages/edit-ticket.html',
        {
            'ticket': ticket,
            'form': form
        }
    )

""" Creates a new ticket and redirects to the home page """
def new_ticket(request):
    if request.method == 'POST':
        form = TicketCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            success(request, 'Ticket created sucessfully.')
            return redirect('tickets:home')
        else:
            error(request, 'Error: invalid form data.')

    return render(
        request,
        'tickets/pages/new-ticket.html',
        {
            'form': form
        }
    )

""" Searches the ticket with the query """
def search_ticket(request):
    query = request.GET.get('q', '')
    tickets = Ticket.objects.all()

    if query.strip():
        """ Search by title or description using the logical OR operator and the django 'Q' """
        tickets = Ticket.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).order_by('-id')
    else:
        tickets = Ticket.objects.none()

    return render(
        request,
        'tickets/pages/search.html',
        {
            'tickets': tickets,
            'query': query
        }
    )
