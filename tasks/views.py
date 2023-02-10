from django.shortcuts import render, redirect

# Create your views here.
def list_task(request):
    return render(request,'list_task.html')

def create_task(request):
    print(request.POST)
    return redirect('/tasks/')