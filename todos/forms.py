from django.forms import ModelForm
from .models import TodoList, TodoItem


class TodoListForm(ModelForm):
  class Meta:
    model = TodoList
    fields = ['name']

class TodoItemForm(ModelForm):
  class Meta:
    model = TodoItem
    fields = '__all__'