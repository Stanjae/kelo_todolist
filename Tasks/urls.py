from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Tasks'
urlpatterns = [
    path('', views.tasklist, name='todo'),
    path('create/', views.createTask, name='create'),
    path('details/<str:pk>/', views.detailTask, name='details'),
    path('update_list/<str:pk>/', views.updateTask, name='update'),
    path('delete_item/<str:pk>/', views.deleteTask, name='delete'),
    path('delete_all/', views.clearlTasks, name='deleteall'),
]
