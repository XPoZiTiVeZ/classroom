from account.models import User
from django.db import models
from uuid import uuid4
from datetime import datetime
from pytz import timezone



class Course(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid4().hex)
    name = models.CharField(unique=True, max_length=32)
    teachers = models.ManyToManyField(User)
    students = models.ManyToManyField(User)
    observers = models.ManyToManyField(User)
    created_at = models.DateField(default=datetime.today())