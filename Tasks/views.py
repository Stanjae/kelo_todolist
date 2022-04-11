from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import TasksList, History
from .forms import TasksListForm
from django.contrib import messages
import random

# Create your views here.

def tasklist(request):
    profile = request.user
    if request.user.is_authenticated:
        taskul = TasksList.objects.all().filter(user = profile)
    else:
        taskul = History.objects.all()
    colors = ['danger','info', 'success','primary', 'secondary','warning']
    mycolor = random.choice(colors)
    context = {'taskul':taskul,'mycolor':mycolor, 'profile':profile}
    return render(request, 'Tasks/index.html', context)

@login_required(login_url="login") 
def createTask(request):
    form = TasksListForm()
    profile = request.user
    if request.method == "POST":
        form = TasksListForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = profile
            messages.success(request, f'Task was sucessfully created')
            project.save()
            
        return redirect('Tasks:todo')
    context = {'form':form}
    return render(request, 'Tasks/create.html', context)



@login_required(login_url="login") 
def detailTask(request, pk):
    profile = request.user
    if profile.is_authenticated:
        taskul = TasksList.objects.all().filter(user = profile).get(id=pk)
    context = {'taskul':taskul}
    return render(request, 'Tasks/detail.html', context)


@login_required(login_url="login") 
def updateTask(request, pk):
    taskupdate = TasksList.objects.get(id=pk)
    form = TasksListForm(instance = taskupdate)
    
    if request.method == "POST":
        form = TasksListForm(request.POST, instance = taskupdate)
        if form.is_valid():
            messages.success(request, f'Task was sucessfully Updated')
            form.save()
            
        return redirect('Tasks:todo')
    context = {'form':form}
    return render(request, 'Tasks/create.html', context)


@login_required(login_url="login") 
def deleteTask(request, pk):
    deleteitem = TasksList.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('Tasks:todo')
    
    context = {'deleteitem':deleteitem}
    return render(request, 'Tasks/delete.html', context)


@login_required(login_url="login") 
def clearlTasks(request):
    profile = request.user
    items = TasksList.objects.all().filter(user = profile)
    if request.method == "POST":
        items.delete()
        return redirect('Tasks:todo')
    context = {'items':items}
    return render(request, 'Tasks/clear.html', context)
