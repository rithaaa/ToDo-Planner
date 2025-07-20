from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from . import forms,models
from . forms import TaskInfo
from django.contrib import messages
# Create your views here.

def Hello(request):
    return HttpResponse("Hello World")

def home(request):
    return  render(request,"home.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import forms

def SignUp(request):
    if request.method == 'POST':
        userForm = forms.PersonUserForm(request.POST)
        detailForm = forms.PersonDetailForm(request.POST)
        if userForm.is_valid() and detailForm.is_valid():
            # Save User model
            user = userForm.save(commit=False)
            raw_password = userForm.cleaned_data['password']
            user.set_password(raw_password)  # hashes password
            user.save()

            # Save Person details
            person = detailForm.save(commit=False)
            person.user = user  # link to User
            person.save()

            return redirect('login')  # Adjust to your URL name
        else:
            print("Form errors:", userForm.errors, detailForm.errors)
    else:
        userForm = forms.PersonUserForm()
        detailForm = forms.PersonDetailForm()

    context = {'userForm': userForm, 'detailForm': detailForm}
    return render(request, 'signup.html', context)

def Dashboard(request):
    task=models.Tasks.objects.all()
    return render(request,'dashboard.html',{'task':task})

def AddTask(request):
    if request.method=='POST':
        addtaskform=TaskInfo(request.POST)
        if addtaskform.is_valid():
            addtaskform.save()
            return redirect('dashboard')
    else:
        addtaskform=TaskInfo()
    return render(request,'Add_Task.html',{'addtaskform':addtaskform})


def Edit(request,pk):
    task=models.Tasks.objects.get(id=pk)
    if request.method=='POST':
        taskform=forms.TaskInfo(request.POST, instance=task)
        if taskform.is_valid():
            taskform.save()
            return redirect('dashboard')
    else:
        taskform=forms.TaskInfo(instance=task)
    return render(request,'edit.html',{'taskform':taskform})

def Delete(request,pk):
    task=models.Tasks.objects.get(id=pk)
    task.delete()
    return redirect('dashboard')

def Forgpass(request):
    if request.method=='POST':
        username=request.POST.get('username')
        new_password=request.POST.get('new_password')
        
        try:
            user=User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request,'Password updated successfully.')
            # return redirect('login')
        
        except User.DoesNotExist:
            messages.error(request,"User not found.!")
            
    return render(request,'forg.html')