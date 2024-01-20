from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm ,DeveloperForm
from .models import Task , Developer
# Create your views here.
def add_developer(request):
    developer_form = DeveloperForm(request.POST or None)
    if developer_form.is_valid():
        developer_form.instance.user = request.user
        task = developer_form.save()
        return redirect('index')
    context = {'form': developer_form}
    return render(request,"add-developer.html",context)

def update_developer(request,developer_id):
    developer = Developer.objects.get(id=developer_id)
    developer_form = DeveloperForm(request.POST or None, instance=developer)
    if developer_form.is_valid():
        developer_form.instance.user = request.user
        developer_form.save()
        return redirect('index')
    context = {'form': developer_form}
    return render(request,"update-developer.html",context)

def delete_developer(request,developer_id):
    developer = Developer.objects.get(id=developer_id)
    developer.delete()
    return redirect('index')
@login_required(login_url='login')
def index(request):
    tasks = Task.objects.filter(user=request.user)
    developers = Developer.objects.all()
    context = {'tasks': tasks, 'developers':developers}
    return render(request,'index.html',context)

def add_project(request):
    task_form = TaskForm(request.POST or None)
    if task_form.is_valid():
        task_form.instance.user = request.user
        task = task_form.save()
        return redirect('index')
    context = {'form': task_form}
    return render(request,"addproject.html",context)

def delete_project(request,project_id):
    task = Task.objects.get(id=project_id,user=request.user)
    task.delete()
    return redirect('index')

def update_project(request,project_id):
    task = Task.objects.get(id=project_id,user=request.user)
    task_form = TaskForm(request.POST or None, instance=task)
    if task_form.is_valid():
        task_form.instance.user = request.user
        task = task_form.save()
        return redirect('index')
    context = {'form': task_form}
    return render(request,"updateproject.html",context)

