from django.shortcuts import render, redirect
from .models import TodoList, TodoItem
from .forms import TodoListForm, TodoItemForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required
def todo_page(request):
    todo_lists = TodoList.objects.filter(user=request.user).order_by('-creation_time')
    todo_form = TodoListForm(request.POST or None)
    if todo_form.is_valid():
        todo_model = todo_form.save(commit=False)
        todo_model.user = request.user
        todo_model.save()
        return redirect('.')
    context = {'todo_lists': todo_lists, 'todo_form': todo_form}
    return render(request, 'todo/todo.html', context=context)

@login_required
def delete_todo_list(request, pk):
    todo_list = TodoList.objects.get(pk=pk)
    todo_list.delete()
    return redirect(reverse('todo'))

@login_required
def items_page(request, pk):
    todo_list = TodoList.objects.get(pk=pk)
    todo_items = TodoItem.objects.filter(todo_list=todo_list).order_by('status', '-creation_time')
    task_form = TodoItemForm(request.POST or None)
    if task_form.is_valid():
        task_model = task_form.save(commit=False)
        task_model.status = False
        task_model.todo_list = todo_list
        task_model.save()
        return redirect(f'./{pk}')
    context = {'todo_list': todo_list, 'task_form': task_form, 'tasks': todo_items}
    return render(request, 'todo/todo_items.html', context=context)


@login_required
def task_complete(request, pk):
    task = TodoItem.objects.get(pk=pk)
    task.status = True
    todo_list_id = task.todo_list.pk
    task.save()
    return redirect(reverse(items_page, args=(todo_list_id,)))


@login_required
def task_not_complete(request, pk):
    task = TodoItem.objects.get(pk=pk)
    task.status = False
    todo_list_id = task.todo_list.pk
    task.save()
    return redirect(reverse(items_page, args=(todo_list_id,)))

@login_required
def task_delete(request, pk):
    task = TodoItem.objects.get(pk=pk)
    todo_list_id = task.todo_list.pk
    task.delete()
    return redirect(reverse(items_page, args=(todo_list_id,)))

