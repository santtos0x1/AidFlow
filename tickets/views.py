from django.shortcuts import render, redirect
from .models import *
from .forms import TicketCreateForm, TicketEditForm

def home(request):
    return render(request, 'tickets/pages/home.html', {"tickets" : Ticket.objects.all().order_by('-id')})

def details(request, uuid):
    ticket = Ticket.objects.get(uuid=uuid)
    return render(request, 'tickets/pages/detail.html', {'ticket': ticket})

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
    return render(request, 'tickets/pages/edit-ticket.html', {'ticket': ticket, 'form': form})

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
    
    return render(request, 'tickets/pages/new-ticket.html', {'form': form})

