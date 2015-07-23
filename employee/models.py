from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
	CATEGORY_CHOICES = (
            ('M','Male'),
            ('F','Female'),
        )
	MARRIAGE_STATUS = (
			('single','Single'),
			('married','Married'),
			('other','Others'),
		)
	dob = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=10,choices=MARRIAGE_STATUS, default='single')
	gender = models.CharField(max_length=9,choices=CATEGORY_CHOICES, default='M')
	user = models.OneToOneField(User)
	place = models.CharField(max_length=200)

class AssignLeave(models.Model):
	employee = models.ForeignKey(User)
	sums = models.IntegerField(default=0, db_column='get_count')
	casual = models.IntegerField(default=0)
	sick = models.IntegerField(default=0)
	optional = models.IntegerField(default=1)
	
	@property
	def get_count(self):
		return int(self.casual+self.sick+self.optional)

def create_profile(sender, instance, created, raw, **kwargs):
	"""Fleshes out the profile for the newly created user"""
	if created:
		profile = Profile(user=instance)
		profile.save()

def create_assign(sender, instance, created, raw, **kwargs):
	"""Fleshes out the assign leave for the newly created user"""
	if created:
		assign_leave = AssignLeave(employee=instance)
		assign_leave.save()

post_save.connect(create_assign, sender=User,
dispatch_uid='users.models.create_assign')

post_save.connect(create_profile, sender=User,
dispatch_uid='users.models.create_profile')