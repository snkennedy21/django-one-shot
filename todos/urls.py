from django.urls import path
from . import views

urlpatterns = [
  path('', views.view_lists, name="todo_list_list"),
  path('<int:pk>', views.todo_list_detail, name="todo_list_detail"),
  path('create/', views.create_todo_list, name="todo_list_create")
]