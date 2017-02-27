from __future__ import unicode_literals

from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Tickets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 50,null=True)
    date = models.DateField(null=True)
    fees = models.IntegerField(default= 150,null=True)
    email = models.EmailField(null=True)
    adult = models.IntegerField(default = 1)
    child = models.IntegerField(default = 0)
    paid = models.BooleanField(default = False)
    mobile = models.BigIntegerField(null=True)

    def calc_fees(self):
        return self.adult*150+self.child*50

    def get_id(self):
        return self.id

class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 50,null=True)
    date = models.DateTimeField(null=True)
    mobile = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)
    content = models.TextField(max_length = 1000)
