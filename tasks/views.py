from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_task(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request,'list_task.html', {'tasks': tasks})

def create_task(request):
    print(request.POST)
    task = Task(tittle = request.POST['tittle'], description = request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('/tasks/')

def update_task (request, task_id):
    get_id = Task.objects.get(id = task_id)
    if form.is_valid():  
        form.save()  
    return redirect('/tasks/')