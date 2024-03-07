from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def customers(request):
    return HttpResponse('<h1>Hello, this is customers</h1>')

def customers2(request):
    return HttpResponse('<h1>Hello, this is customers2</h1>')