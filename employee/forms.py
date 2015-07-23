from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from employee.models import *

class MyAuthenticationForm(AuthenticationForm):
	username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control form-sign','placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-sign','placeholder':'Password'}), max_length=50)	

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Username'}))
	first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Firstname'}))
	last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Lastname'}))
 	email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Email'}))
 	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-align','placeholder':'Password'}), max_length=50)
 	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-align','placeholder':'Re enter password'}), max_length=50)

 	def clean_username(self):
 		try:
 			user = User.objects.get(username__iexact=self.cleaned_data['username'])
 		except User.DoesNotExist:
 			return self.cleaned_data['username']
 		raise forms.ValidationError('The user already exists')

 	def clean(self):
 		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
 			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
 				raise forms.ValidationError('passwords does not match')
 			else:
 				return self.cleaned_data

class EditUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
	CATEGORY_CHOICES = (
            ('M','Male'),
            ('F','Female'),
        )
	gender = forms.ChoiceField(widget=forms.RadioSelect,choices=CATEGORY_CHOICES)
	class Meta:
		model=Profile
		fields = ('place','gender','status','dob')

class AssignLeaveForm(forms.ModelForm):
	class Meta:
		model = AssignLeave

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()