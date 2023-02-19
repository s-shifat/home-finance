from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_page, name='todo'), 
    path('tasks/<str:pk>', views.items_page, name='tasks'), 
    path('delete_todo_list/<str:pk>', views.delete_todo_list, name='delete_todo_list'), 
    path('task_complete/<str:pk>', views.task_complete, name='task_complete'), 
    path('task_not_complete/<str:pk>', views.task_not_complete, name='task_not_complete'), 
    path('task_delete/<str:pk>', views.task_delete, name='task_delete'), 
]
