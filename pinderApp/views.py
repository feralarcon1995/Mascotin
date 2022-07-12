from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def landing(request):
    return render(request,"pinderApp/index.html") 

def feed(request):
    data = Post.objects.all()
    context = {'data': data}
    return render(request,"pinderApp/feed.html", context) 

def profile(request):
    return render(request,"pinderApp/profile.html")    