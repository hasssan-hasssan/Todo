from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from app.models import Task
from app.forms import UpdateTaskForm


def taskList(request):
    user = request.user
    todo_list = user.task_set.all()
    return render(request, 'list.html', {'todo_list':todo_list})


def taskUpdate(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid:
            task = form.save()
            task.save()
            messages.success(request, 'Task successfully updated !')
            return redirect('taskList')
    else:
        form = UpdateTaskForm(instance=task)
        
    return render(request, 'update.html', {'task':task, 'form':form,})


def taskDelete(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        messages.error(request, f"Task by ID: {id} does not exist!")
        return redirect('taskList')
    else:
        try:
            task.delete()
        except:
            messages.error(request, "Delete task failed please try again")
            return redirect('taskList')
        else:
            messages.success(request, "Task successfully deleted")
            return redirect('taskList')