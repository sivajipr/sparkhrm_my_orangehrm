from django.contrib import admin
from leave.models import *
# Register your models here.

class LeaveAdmin(admin.ModelAdmin):
	list_display = ('employee','leave_type','from_date','to_date','comment','status')

admin.site.register(Leave, LeaveAdmin)

