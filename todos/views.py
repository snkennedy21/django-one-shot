from django.shortcuts import redirect, render
from .models import TodoList, TodoItem
from .forms import TodoListForm



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


def create_todo_list(request):
  form = TodoListForm()

  if request.method == "POST":
    form = TodoListForm(request.POST)
    if form.is_valid():
      list_details = form.save()

      return redirect('todo_list_detail', list_details.pk)

  context = {
    'form': form
  }
  return render(request, 'todos/create.html', context)