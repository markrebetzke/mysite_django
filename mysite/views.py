from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('Hello Mofo')

def home(requests):
    return render(requests, 'home.html')
    #return HttpResponse('Hello Home')
