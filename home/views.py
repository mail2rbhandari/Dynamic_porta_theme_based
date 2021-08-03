from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is a home page')
def tem2(request):
    return render(request, 'tem2.html')
def tutorial(request):
    return render(request, 'tutorial.html')
def robin(request):
    return HttpResponse('This is robin')
def about(request):
    return HttpResponse('This is about page')
def services(request):
    return HttpResponse('This is services page')
def contact(request):
    return HttpResponse('This is contact page')
def FB(request):
    return HttpResponse('This is FB page')
#URL disapting is understood..
#let us use templates now...

# Create your views here.
