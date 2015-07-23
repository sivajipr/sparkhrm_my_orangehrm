from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Leave(models.Model):
	LEAVE_TYPE = (
			('casual','Casual Leave'),
			('sick','Sick Leave'),
			('optional','Optional leave'),
		)
	employee = models.ForeignKey(User)
	leave_type = models.CharField(max_length=10,choices=LEAVE_TYPE)
	from_date = models.DateField(null=True, blank=True)
	to_date = models.DateField(null=True, blank=True)
	comment = models.TextField(max_length=100)
	status = models.IntegerField(default=0)
	leave_days = models.IntegerField(default=0)
