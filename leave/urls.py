from django.conf.urls import patterns, include, url
import views
from django.conf import settings
import leave
urlpatterns = patterns('',

    # url(r'^', 'django.contrib.auth.views.login'),
    url(r'leave/apply', leave.views.apply_leave),
    url(r'leave/pending', leave.views.pending_leave),
    url(r'leave/myleave', leave.views.my_leave),
    url(r'leave/(?P<id>[0-9]{1,})/accept', leave.views.accept_leave),
    url(r'leave/(?P<id>[0-9]{1,})/reject', leave.views.reject_leave),
    url(r'leave/(?P<id>[0-9]{1,})/admin-summery', leave.views.admin_summery),
	)