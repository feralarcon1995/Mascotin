from multiprocessing import context
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
        data = Post.objects.all()
        context = {'data': data}
        return render(request, "pinderApp/feed.html", context)

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post creado con exito.')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, "pinderApp/post.html", {'form': form})

    
@login_required
def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
     user = User.objects.get(username=username)
     posteos = user.posteos.all()
    else:
     posteos = current_user.posteos.all()
     user = current_user
    return render(request, 'pinderApp/profile.html', {'user':user, 'posteos':posteos})

@login_required
def editProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)
    user__basic__info = User.objects.get(id=user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES , instance=profile)
        if form.is_valid():
          user__basic__info.first_name= form.cleaned_data.get('first_name')
          user__basic__info.last_name= form.cleaned_data.get('last_name') 
          user__basic__info.username= form.cleaned_data.get('username') 
          user__basic__info.email= form.cleaned_data.get('email') 
          
          profile.image = form.cleaned_data.get('image')
          profile.dni = form.cleaned_data.get('dni')
          profile.sexo = form.cleaned_data.get('sexo')
          profile.edad = form.cleaned_data.get('edad')
          profile.telefono = form.cleaned_data.get('telefono')
          profile.localidad = form.cleaned_data.get('localidad')
          profile.provincia = form.cleaned_data.get('provincia')
          profile.ocupacion = form.cleaned_data.get('ocupacion')
          profile.carga_horaria = form.cleaned_data.get('carga_horaria')
          profile.dias_homeoffice = form.cleaned_data.get('dias_homeoffice')
          profile.cantidad_hijos = form.cleaned_data.get('cantidad_hijos')
          profile.espacio_abierto = form.cleaned_data.get('espacio_abierto')

          profile.save()
          user__basic__info.save()
          messages.success(request, f'Perfil actualizado con exito.')
          return redirect('profile', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=profile)
    
    context={
      'form':form,
    } 
    return render(request, "pinderApp/profile_form.html", context)


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

    


# if request.method == 'PÓST':
#         u_form= UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, 
#                                    request.FILES, 
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()    
#             messages.success(request, f'Perfil actualizado con exito.')
#             return redirect('profile')
                       
#     else:
#         u_form= UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,     
#         }