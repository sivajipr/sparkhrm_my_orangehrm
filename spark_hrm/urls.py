from django.conf.urls import patterns, include, url
from django.contrib import admin
import employee
from employee.forms import MyAuthenticationForm
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spark_hrm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('employee.urls')),
    url(r'^', include('leave.urls')),
    url(r'^login', 'django.contrib.auth.views.login',{'authentication_form':MyAuthenticationForm}),
    url(r'^home', 'employee.views.home'),
    # url(r'^', 'django.contrib.auth.views.login'),
    # url(r'home', 'views.home'),
)
