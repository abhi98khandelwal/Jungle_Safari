"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from app.models import Tickets,Feedback

class Ticket_Form(ModelForm):
    class Meta:
        model = Tickets
        fields = ["name","date","mobile","email","adult","child"]

class Feedback_Form(ModelForm):
    class Meta:
        model = Feedback
        fields = ["name","mobile","email","content"]