from django.shortcuts import render, redirect
from .models import Simple_Project

def todo_list(request):
    todos = Simple_Project.objects.all()
    return render(request, 'simple_project/templates/todo.html', {'todos': todos})

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        Simple_Project.objects.create(title=title)
        return redirect('todo')
    return render(request, 'simple_project/templates/add_task.html')

def complete_task(request, todo_id):
    todo = Simple_Project.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo')

def delete_completed_tasks(request):
    Simple_Project.objects.filter(completed=True).delete()
    return redirect('todo')
    