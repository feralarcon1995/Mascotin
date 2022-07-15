from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.


def landing(request):
    return render(request,"pinderApp/index.html") 

def about(request):
    return render(request,"pinderApp/about.html")    

def feed(request):
    if request.user.is_authenticated:
        data = Post.objects.all()
        context = {'data': data}
        return render(request,"pinderApp/feed.html", context) 
    else:
        return render(request, "pinderApp/index.html")  
       
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request,'Post enviado con exito.')
            return redirect('Feed')
    else:
        form = PostForm()
    return render(request, "pinderApp/post.html", {'form':form})    


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
