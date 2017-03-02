from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from .forms import Ticket_Form,Feedback_Form
from django.conf import settings
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect

# Create your views here.

def home(request):
    """Renders Home Page"""
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'home.html',
        {
            'title':"Home Page",
            'year':datetime.now().year,
         }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'layout.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def buyticket(request):
    """Renders the about page."""
    if request.method == "POST":
        ticket_form = Ticket_Form(request.POST)
        if ticket_form.is_valid():
            post_ticket_form = ticket_form.save(commit = False)
            post_ticket_form.fees = post_ticket_form.adult*150 + post_ticket_form.child*5
            post_ticket_form.save()
            return HttpResponseRedirect('/')
    else:
        ticket_form = Ticket_Form()

    return render(
        request,
        'tickets.html',
        {
            'title':'BuyTicket',
            'year':datetime.now().year,
            'ticket_form' : ticket_form}
    )

def feedback(request):
    if request.method == "POST":
        feedback_form = Feedback_Form(request.POST)
        if feedback_form.is_valid():
            f = feedback_form.save()
            send_mail(
    "Feedback of "+str(f.name)+" "+str(f.mobile)+" "+str(f.email),
    f.content,
    settings.EMAIL_HOST_USER,
    ['wolfwebstreet@gmail.com'],
    fail_silently=False,
)
            return HttpResponseRedirect('/')
    else:
        feedback_form = Feedback_Form()
    return render(
        request,
        'contact.html',
        {
            'title':'Feedback',
            'feedback_form' : feedback_form}
    )
