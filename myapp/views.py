# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("index hello world")


def hello(request, username):
    return HttpResponse("hello %s" % username)

def id(request, id):
    return HttpResponse("id: %s" % id)
    
def projects(request):
    # Get all projects.
    projects = list(Projects.objects.values())

    return JsonResponse(projects, safe=False)
    
def task(request, id):
    #Get by id or return 404.
    task = get_object_or_404(Task, id = id)
    
    return HttpResponse("task: %s" % task.title)
    