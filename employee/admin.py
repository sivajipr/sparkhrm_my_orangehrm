from django.contrib import admin
from employee.models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'place','gender','status','dob')

class AssignLeaveAdmin(admin.ModelAdmin):
	list_display = ('employee','casual','sick','optional')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(AssignLeave, AssignLeaveAdmin)