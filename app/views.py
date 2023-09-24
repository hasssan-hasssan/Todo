from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def todoList(request):
    user = request.user
    todo_list = user.task_set.all()
    return render(request, 'list.html', {'todo_list':todo_list})
