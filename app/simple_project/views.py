from django.shortcuts import render, redirect
from .models import Simple_Project

def todo_list(request):
    todos = Simple_Project.objects.all()
    return render(request, 'todo.html', {'todos': todos})

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        Simple_Project.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'add_task.html')

def complete_task(request, todo_id):
    todo = Simple_Project.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def completed_tasks(request):
    completed_tasks = Simple_Project.objects.filter(completed=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})
    