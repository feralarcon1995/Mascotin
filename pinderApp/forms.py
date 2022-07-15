from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="Ingrese su nombre")
    last_name = forms.CharField(max_length=100, label="Ingrese su apellido")
    username = forms.CharField(max_length=50, label="Ingrese su nombre de usuario")
    email = forms.EmailField(label="Ingrese su email",widget=forms.EmailInput)
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        help_texts={k:"" for k in fields}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nombre','especie','imgPosteo','sexo','edad','tamanio','vacunas_aplicadas','castracion','desparasitado','discapacidad','content']
  
           

        
        
# 

