from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.


def landing(request):
    return render(request,"pinderApp/index.html") 

def feed(request):
    data = Post.objects.all()
    context = {'data': data}
    return render(request,"pinderApp/feed.html", context) 

def profile(request):
    return render(request,"pinderApp/profile.html")    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            messages.success(request, f'Hola {name}, tu usuario se creo con exito.')
            return redirect('Feed')
    else:
        form = UserRegisterForm()

    context= { 'form' : form }           
    return render(request, "pinderApp/register.html",context)
