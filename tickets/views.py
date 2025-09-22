from django.shortcuts import render, redirect
from .models import *
from .forms import TicketCreateForm, TicketEditForm, ReplyTicketForm
from django.contrib import messages

def get_started(request):
    return render(request, 'tickets/pages/get-started.html')

def home(request):
    return render(request, 'tickets/pages/home.html', {
        "tickets" : Ticket.objects.all().order_by('-id')
    })

def details(request, uuid):
    ticket = Ticket.objects.get(uuid=uuid)
    return render(request, 'tickets/pages/detail.html', {
        'ticket': ticket
    })

def delete_ticket(request, uuid):
    ticket = Ticket.objects.get(uuid=uuid)
    if request.method == 'POST' and request.POST.get('action') == 'delete_confirm':
        ticket.delete()
        messages.success(request, 'Ticket deleted successfully.')
        return redirect('tickets:home')
    
    return render(request, 'tickets/detail.html', {'ticket': ticket})
    

def reply_ticket(request, uuid):
    ticket = Ticket.objects.get(uuid=uuid)
    form = ReplyTicketForm(request.POST, instance=ticket)
    if request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            form.save()
            return redirect('tickets:detail', uuid=ticket.uuid)
        else:
            form = ReplyTicketForm(instance=ticket)
    return render(request, 'tickets/pages/reply-page.html', {
        'ticket': ticket,
        'form': form
    })

def edit_ticket(request, uuid):
    ticket = Ticket.objects.get(uuid=uuid)
    form = TicketEditForm(request.POST, instance=ticket)
    if request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user 
            form.save()
            return redirect('tickets:home')
        else:
            form = TicketEditForm(instance=ticket)
    return render(request, 'tickets/pages/edit-ticket.html', {
        'ticket': ticket,
        'form': form
    })

def new_ticket(request):
    if request.method == 'POST':
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user 
            form.save()
            return redirect('tickets:home')
    else:
        form = TicketCreateForm()
    
    return render(request, 'tickets/pages/new-ticket.html', {
        'form': form
    })

def search_ticket(request):
    query = request.GET.get('q', '')
    if query:
        tickets = Ticket.objects.filter(title__icontains=query)
    else:
        tickets = Ticket.objects.all()
        
    return render(request, 'tickets/pages/search.html', {
        'tickets': tickets
    })
    