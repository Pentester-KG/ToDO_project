from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/todolist/', views.tasks_list_api_view, name='todolist'),
    path('api/v1/todolist/<int:id>/', views.task_detail_api_view, name='task_detail')
]