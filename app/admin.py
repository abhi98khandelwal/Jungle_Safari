from django.contrib import admin
from app.models import Tickets,Feedback

class Ticket_admin(admin.ModelAdmin):
    list_display = ["id","name","date","mobile","email","fees","adult","child","paid"]
    list_filter = ("date","adult","child","paid")
    date_hierarchy = 'date'

class Feedback_admin(admin.ModelAdmin):
    list_display = ["id","name","mobile","email","content"]
    list_filter = ["date"]

admin.site.register(Tickets,Ticket_admin)
admin.site.register(Feedback,Feedback_admin)
