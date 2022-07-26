from django.urls import path
from .views import todo_list_detail, view_lists

urlpatterns = [
  path('', view_lists, name="todo_list_list"),
  path('<int:pk>', todo_list_detail, name="todo_list_detail")
]