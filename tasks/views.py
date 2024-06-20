from django.shortcuts import render
from django.views.generic import ListView
from .models import Tasks
# Create your views here.
def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/task_list.html',{'tasks': tasks})

class TaskListView(ListView):
    Model = Tasks
    tamplate_name = 'tasks/task_list.html'
    