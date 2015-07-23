from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Salary(models.Model):
	employee = models.ForeignKey(User)
	amount = models.IntegerField(default=0)