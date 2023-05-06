from django.shortcuts import render
from django.http import *

# Create your views here.
def print(request):

    return render(request,'valeos/index.html')
