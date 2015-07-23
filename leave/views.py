from django.shortcuts import render,render_to_response
from leave.forms import LeaveForm
from leave.models import Leave
from employee.models import AssignLeave
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.db.models import Q
from datetime import date

def apply_leave(request):
	user=request.user
	admins = User.objects.filter(is_staff=True)
	if request.method == 'POST':
		form = LeaveForm(request.POST)
		if form.is_valid():
			casual_leave_days=0
			sick_leave_days=0
			optional_leave_days=0
			assign_leave = AssignLeave.objects.get(employee=user)
			leave = Leave(employee=request.user,
						  leave_type=form.cleaned_data['leave_type'],
						  from_date=form.cleaned_data['from_date'],
						  to_date=form.cleaned_data['to_date'],
						  comment=form.cleaned_data['comment'])
			d1 = date(leave.from_date.year,leave.from_date.month,leave.from_date.day)
			d0 = date(leave.to_date.year,leave.to_date.month,leave.to_date.day)
			leave.leave_days=(d0-d1).days
			if leave.leave_type=='casual':
				casual_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='casual',employee=user)
				for i in casual_leave_times:
					casual_leave_days+=i.leave_days
				casual_leave_diff = assign_leave.casual-casual_leave_days
				if casual_leave_diff>0:
					leave.save()
			elif leave.leave_type=='sick':
				sick_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='sick',employee=user)
				for i in sick_leave_times:
					sick_leave_days+=i.leave_days
				sick_leave_diff = assign_leave.sick-sick_leave_days
				if sick_leave_diff>0:
					leave.save()
			elif leave.leave_type=='optional':
				optional_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='optional',employee=user)
				for i in optional_leave_times:
					optional_leave_days+=i.leave_days
				optional_leave_diff = assign_leave.optional-optional_leave_days
				if optional_leave_diff>0:
					leave.save()
			else:
				return
			#send_mail('Leave application', '%s applied a leave from' %request.user, 'sivaji@sparksupport.com',
						# [admin.email for admin in admins],fail_silently=False)
			return HttpResponseRedirect('/home')
	else:
		form = LeaveForm()
	variables = RequestContext(request, {
    'form': form
    })

    	return render_to_response('leave/apply_leave.html',variables)

@user_passes_test(lambda u:u.is_staff, login_url='/login')
def pending_leave(request):
	leaves=Leave.objects.filter(status=0)
	return render(request,'leave/pending_leave.html',{'leaves':leaves})

def accept_leave(request,id):
	leave=Leave.objects.get(id=id)
	# send_mail('leave', 'Your leave is approved', 'sivaji@sparksupport.com',
    # [leave.employee.email],fail_silently=False)
	leave.status=1
	leave.save()
	return HttpResponseRedirect('/leave/pending')

def reject_leave(request,id):
	leave=Leave.objects.get(id=id)
	leave.status=2
	leave.save()
	return HttpResponseRedirect('/leave/pending')

def my_leave(request):
	leaves = Leave.objects.filter(employee=request.user)
	return render(request,'leave/myleave.html',{'leaves':leaves})

def admin_summery(request,id):
    user=User.objects.get(id=id)
    casual_leave_days=0
    sick_leave_days=0
    optional_leave_days=0
    employee=User.objects.get(username=user)
    assign_leave = AssignLeave.objects.get(employee=user)
    casual_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='casual',employee=user)
    sick_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='sick',employee=user)
    optional_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='optional',employee=user)
    casual_leave_taken = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='casual',employee=user).count()
    sick_leave_taken = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='sick',employee=user).count()
    optional_leave_taken = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='optional',employee=user).count()
    for i in casual_leave_times:
        casual_leave_days+=i.leave_days
    for i in sick_leave_times:
        sick_leave_days+=i.leave_days
    for i in optional_leave_times:
        optional_leave_days+=i.leave_days
    casual_leave_diff = assign_leave.casual-casual_leave_days
    sick_leave_diff = assign_leave.sick-sick_leave_days
    optional_leave_diff = assign_leave.optional-optional_leave_days
    return render(request,'leave/summery.html',{'employee':employee, 'assign_leave':assign_leave,
                                                'casual_leave_taken':casual_leave_taken,
                                                'sick_leave_taken':sick_leave_taken,
                                                'optional_leave_taken':optional_leave_taken,
                                                'casual_leave_diff':casual_leave_diff,
                                                'sick_leave_diff':sick_leave_diff,
                                                'optional_leave_diff':optional_leave_diff})

