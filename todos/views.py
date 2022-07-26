from django.shortcuts import render
from .models import TodoList, TodoItem


def view_lists(request):
  lists = TodoList.objects.all()
  context = {
    "lists": lists
  }

  return render(request, 'todos/list.html', context)


def todo_list_detail(request, pk):
  todo_list = TodoList.objects.get(id=pk)
  context = {
    "list": todo_list
  }

  return render(request, 'todos/detail.html', context)