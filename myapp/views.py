# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title="Django app"

    return render(request, "index.html", {
        "title": title
    })


def hello(request, username):
    return HttpResponse("hello %s" % username)

def id(request, id):
    return HttpResponse("id: %s" % id)
    
def projects(request):
    # Get all projects.
    projects_list = list(Projects.objects.values())
    projects =  Projects.objects.all()

    # return JsonResponse(projects, safe=False)
    return render(request, "projects.html", {
        "projects": projects,
        "project_list": projects_list
    })

def task(request):
    #Get by id or return 404.
    # task = get_object_or_404(Task, id = id)
    
    task = Task.objects.all()
    
    # return HttpResponse("task: %s" % task.title)
    return render(request, "task.html", {
        "task": task
    })