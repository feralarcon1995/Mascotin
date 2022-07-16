from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def landing(request):
    return render(request, "pinderApp/index.html")


def about(request):
    return render(request, "pinderApp/about.html")

@login_required
def feed(request):
    if request.user.is_authenticated:
        data = Post.objects.all()
        context = {'data': data}
        return render(request, "pinderApp/feed.html", context)
    else:
        return render(request, "pinderApp/index.html")

@login_required
def post(request):
  if request.user.is_authenticated:
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado con exito.')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, "pinderApp/post.html", {'form': form})
  else:
    return redirect('login')
    

@login_required
def profile(request, username=None):
    if request.user.is_authenticated:
     current_user = request.user
     if username and username != current_user.username:
         user = User.objects.get(username=username)
         posts = user.posts.all()
     else:
         posts = current_user.posts.all()
         user = current_user
     return render(request, "pinderApp/profile.html", {'user': user, 'posts': posts})
    else:
     return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('feed')
    else:
        if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             user = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password1')
             username = authenticate(username=user, password=password)
             login(request, username)
             messages.success( request, f'Hola {user}, tu usuario se creo con exito.')
             return redirect('feed')
        else:
          form = UserRegisterForm()
          context = {'form': form}
          return render(request, "pinderApp/register.html", context)    

    
