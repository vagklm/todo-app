from django.urls import path
from simple_project import views

urlpatterns = [
    path('todo_app/', views.todo_list, name='todo_list'),
    path('todo_app/add/', views.add_task, name='add_task'),
    path('todo_app/complete/<int:todo_id>/', views.complete_task, name='complete_task'),
    path('todo_app/completed_tasks/', views.completed_tasks, name='completed_tasks'),
]