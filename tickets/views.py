import logging

from django.contrib.messages import success, error
from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Ticket
from .forms import ReplyTicketForm, TicketEditForm, TicketCreateForm

logger = logging.getLogger(__name__)


def check_form_request_and_validate(request, form, message, redir, ticket_uuid=None):
    if request.method != 'POST':
        return None

    try:
        if form.is_valid():
            form.save()
            success(request, message)
            if ticket_uuid:
                return redirect(redir, uuid=ticket_uuid)
            return redirect(redir)
        error(request, 'Error: invalid form data.')
    except Exception as err:
        logger.exception(f'Unexpected error while processing form: {err}')
        error(request, 'Internal error: could not process form.')

    return None


def get_ticket_by_uuid_or_404(uuid):
    return Ticket.objects.get_by_uuid_or_404(uuid=uuid)


def get_started(request):
    return render(
        request,
        'tickets/pages/get-started.html'
    )


def home(request):
    tickets = Ticket.objects.all()
    return render(
        request,
        'tickets/pages/home.html',
        {
            'tickets': tickets
        }
    )


def details(request, uuid):
    ticket = get_ticket_by_uuid_or_404(uuid=uuid)
    return render(
        request,
        'tickets/pages/detail.html',
        {
            'ticket': ticket
        }
    )


def delete_ticket(request, uuid):
    ticket = get_ticket_by_uuid_or_404(uuid=uuid)

    if request.method == 'POST':
        try:
            if request.POST.get('action') == 'delete_confirm':
                ticket.delete()
                success(request, 'Ticket deleted successfully.')
                return redirect('tickets:home')
        except Exception as err:
            logger.exception(f'Could not delete the ticket: {err}')
            error(request, 'Error on ticket delete, ticket not deleted.')

    return render(
        request,
        'tickets/pages/detail.html',
        {
            'ticket': ticket
        }
    )


def reply_ticket(request, uuid):
    ticket = get_ticket_by_uuid_or_404(uuid=uuid)
    form = ReplyTicketForm(request.POST or None, instance=ticket)

    response = check_form_request_and_validate(
        request=request,
        form=form,
        message='Ticket replied successfully.',
        redir='tickets:detail',
        ticket_uuid=ticket.uuid
    )

    if response:
        return response

    return render(
        request,
        'tickets/pages/reply-page.html',
        {
            'ticket': ticket,
            'form': form
        }
    )


def edit_ticket(request, uuid):
    ticket = get_ticket_by_uuid_or_404(uuid=uuid)
    form = TicketEditForm(request.POST or None, instance=ticket)

    response = check_form_request_and_validate(
        request=request,
        form=form,
        message='Ticket edited successfully.',
        redir='tickets:detail',
        ticket_uuid=ticket.uuid
    )

    if response:
        return response

    return render(
        request,
        'tickets/pages/edit-ticket.html',
        {
            'ticket': ticket,
            'form': form
        }
    )


def new_ticket(request):
    form = TicketCreateForm(request.POST or None)

    response = check_form_request_and_validate(
        request=request,
        form=form,
        message='Ticket created successfully.',
        redir='tickets:home'
    )

    if response:
        return response

    return render(
        request,
        'tickets/pages/new-ticket.html',
        {
            'form': form
        }
    )


def search_ticket(request):
    query = request.GET.get('q', '').strip()
    tickets = Ticket.objects.none()

    try:
        if query:
            tickets = Ticket.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            ).order_by('-id')
    except Exception as err:
        logger.exception(f'Query error: {err}')

    return render(
        request,
        'tickets/pages/search.html',
        {
            'tickets': tickets,
            'query': query
        }
    )
