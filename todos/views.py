from django.shortcuts import render
from .models import TodoList, TodoItem


def view_lists(request):
  lists = TodoList.objects.all()
  context = {
    "lists": lists
  }

  return render(request, 'todos/list.html', context)
