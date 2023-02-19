from django import forms
from .models import TodoList, TodoItem

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['list_name']
        widgets = {
                'list_name': forms.TextInput(attrs={'class':'form-control'})
        }


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['item_name']
        widgets = {
                'item_name': forms.TextInput(attrs={'class':'form-control'})
        }

