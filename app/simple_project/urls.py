from django.urls import path
from simple_project import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:todo_id>/', views.complete_task, name='complete_task'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
]