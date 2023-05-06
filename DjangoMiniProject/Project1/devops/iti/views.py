from django.shortcuts import render
from django.http import *

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")


courses = ["ansible", "Django", "Docker", "Python"]
def getCourses(request):
    return  HttpResponse(f"<ol> <h4>{courses[0]}</h4>"
                         f" <h4>{courses[1]}</h4>"
                         f" <h4>{courses[2]}</h4>"
                         f" <h4>{courses[3]}</h4>"
                         f"</ol>")
def getCourseByID(request,idx):
    idx = int(idx)
    if idx in range(len(courses)):
        return HttpResponse(f"<h4>{courses[idx]}</h4>")
    else:
        return HttpResponseNotFound("<h1>course not found</h1>")

