from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_task(request):
    return render(request,'list_task.html')

def create_task(request):
    print(request.POST)
    task = Task(tittle=request.POST['tittle'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')
