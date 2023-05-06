from django.shortcuts import render
from django.http import *
# Create your views here.
def printing(request):
    # return HttpResponse("Students!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return render(request,'students/index.html')


