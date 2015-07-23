from django import forms
from django.contrib.auth.models import User
from leave.models import *

class LeaveForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(attrs={'cols': '20','rows':'5'}))
	class Meta:
		model = Leave
		fields = ('leave_type','from_date','to_date','comment')

