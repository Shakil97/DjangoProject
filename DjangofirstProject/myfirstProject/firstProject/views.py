from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def help(request):
    my_dict = {"hello i m from views.py"}
    return HttpResponse(request,'firstApp/index.html',context=my_dict)