# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index hello world")


def hello(request, username):
    return HttpResponse("hello %s" % username)

def id(request, id):
    return HttpResponse("id: %s" % id)