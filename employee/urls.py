from django.conf.urls import patterns, include, url
import views
from django.conf import settings
urlpatterns = patterns('',

    # url(r'^', 'django.contrib.auth.views.login'),
    url(r'register', 'employee.views.register'),
    url(r'logout', 'employee.views.log_out'),
    url(r'employee/assign', 'employee.views.assign'),
	url(r'employee/value/', 'employee.views.get_employee_details'),
	url(r'leave/summery', 'employee.views.summery'),
	url(r'leave/adminsummery', 'employee.views.adminsummery'),
	url(r'employee/upload', 'employee.views.uploading'),
	url(r'employee/list', 'employee.views.list_user'),
	)