from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from app.models import Task
from app.forms import UpdateTaskForm, CreateTaskForm
from app import strConst


def taskList(request):
    user = request.user
    todo_list = user.task_set.all().order_by('-create')
    return render(request, 'list.html', {'todo_list':todo_list})


def taskUpdate(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid:
            task = form.save()
            try:
                task.save()
                messages.success(request, strConst.TASK_UPDATE_SUCCESS)
                return redirect('taskList')
            except:
                messages.error(request, strConst.TASK_UPDATE_FAIL)
                return redirect('taskList')
    else:
        form = UpdateTaskForm(instance=task)
        
    return render(request, 'update.html', {'task':task, 'form':form,})


def taskDelete(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        messages.error(request, strConst.TASK_NOT_FOUND)
        return redirect('taskList')
    else:
        try:
            task.delete()
        except:
            messages.error(request, strConst.TASK_DELETE_FAIL)
            return redirect('taskList')
        else:
            messages.success(request, strConst.TASK_DELETE_SUCCESS)
            return redirect('taskList')
        
        
def taskCreate(request):
    user = request.user
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            try:
                new_task = form.save(commit=False)
                new_task.author = user
                new_task.save()
                messages.success(request,strConst.TASK_CREATE_SUCCESS)
                return redirect('taskList')
            except:
                messages.error(request, strConst.TASK_CREATE_FAIL)
                return redirect('taskList')
    else:
        form = CreateTaskForm()
    
    return render(request, 'create.html', {'form':form, })

   