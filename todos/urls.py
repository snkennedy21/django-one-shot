from django.urls import path
from . import views


urlpatterns = [
  path('', views.view_lists, name="todo_list_list"),
  path('<int:pk>', views.todo_list_detail, name="todo_list_detail"),
  path('create/', views.create_todo_list, name="todo_list_create"),
  path('<int:pk>/edit/', views.update_todo_list, name="todo_list_update"),
  path('<int:pk>/delete/', views.delete_todo_list, name="todo_list_delete"),
  path('items/create/', views.create_item, name="todo_item_create"),
  path('items/<int:pk>/edit/', views.update_item, name="todo_item_update")
]