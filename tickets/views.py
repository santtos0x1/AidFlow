from django.shortcuts import render, redirect
from .models import *
from .forms import TicketForm

def home(request):
    return render(request, 'tickets/pages/home.html', {"tickets" : Ticket.objects.all().order_by('-id')})

def details(request, uuid):
    ticket = Ticket.objects.get(uuid=uuid)
    return render(request, 'tickets/pages/detail.html', {'ticket': ticket})

def new_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user 
            form.save()
            return redirect('tickets:home')
    else:
        form = TicketForm()
    
    return render(request, 'tickets/pages/new-ticket.html', {'form': form})