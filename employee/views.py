import json
from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from employee.forms import RegisterForm, ProfileForm, EditUserForm, AssignLeaveForm, UploadFileForm
from django.contrib.auth import login, logout
from employee.models import Profile, AssignLeave
from leave.models import Leave
from django.db.models import Q
import csv
from codecs import EncodedFile
def home(request):
    user = request.user
    admins = User.objects.filter(is_staff=True)
    users = User.objects.get(username=user)
    profile = Profile.objects.get(user=user)
    if user.is_authenticated():
    	if request.method == 'POST':
            form1 = EditUserForm(request.POST, instance=users)
            form2 = ProfileForm(request.POST, instance=profile)
            if form1.is_valid() and form2.is_valid():
                form2.save()
                form1.save()
                return HttpResponseRedirect('/home')
    	else:
        	form1 = EditUserForm(instance=users)
        	form2 = ProfileForm(instance=profile)

    	variables = RequestContext(request, {'user':user, 'admins':admins,'form1': form1, 'form2':form2})
 
    	return render_to_response(
    'employee/home.html',
    variables,
    )


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], password=form.cleaned_data['password1'], last_name=form.cleaned_data['last_name'])
            return HttpResponseRedirect('/home')
    else:
        form = RegisterForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'employee/register.html',
    variables,
    )

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')

def assign(request):
    user=request.user
    assign = AssignLeave.objects.get(employee=user)
    if request.method == 'POST':
        form = AssignLeaveForm(request.POST, instance=assign)
        if form.is_valid():
            assi = AssignLeave.objects.get(employee=form.cleaned_data['employee'])
            form = AssignLeaveForm(request.POST, instance=assi)
            form.save()
            return HttpResponseRedirect('/home')
    else:
        form = AssignLeaveForm(instance=assign)

    variables = RequestContext(request, {'form': form})
 
    return render_to_response(
    'employee/assign.html',
    variables,
    )

def get_employee_details(request):
    emplo=User.objects.filter(id=request.GET['id'])
    assignleave=AssignLeave.objects.get(employee=emplo)
    data=json.dumps({'sick':assignleave.sick,'casual':assignleave.casual,'optional':assignleave.optional})
    return HttpResponse(data, content_type="application/json")

def summery(request):
    user=request.user
    casual_leave_days=0
    sick_leave_days=0
    optional_leave_days=0
    employee=User.objects.get(username=user)
    assign_leave = AssignLeave.objects.get(employee=user)
    casual_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='casual',employee=user)
    sick_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='sick',employee=user)
    optional_leave_times = Leave.objects.filter(Q(status=0)|Q(status=1),leave_type='optional',employee=user)
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

def adminsummery(request):
    employees = User.objects.all()
    return render(request,'leave/adminsummery.html',{'employees':employees})

def uploading(request):
    if request.method == 'POST':
        print 0
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print 1
            filess = request.FILES['file'].open()
            records = csv.DictReader(EncodedFile(filess,'utf-8'))
            for row in records:
                user = User.objects.create_user(username=row['username'],
                                                    first_name=row['first_name'],
                                                    last_name=row['last_name'],
                                                    email=row['email'],
                                                    password=row['password'])
            return HttpResponseRedirect('/home')
    else:
        form = UploadFileForm()
    return render(request,'employee/upload.html', {'form': form})

def list_user(request):
    users = User.objects.all()
    with open('static/files/names.csv', 'w') as csvfile:
        fieldnames = ['username','first_name', 'last_name','email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow({'username':user.username, 'first_name': user.first_name,
                             'last_name': user.last_name, 'email': user.email})
        return render(request,'employee/user-list.html')