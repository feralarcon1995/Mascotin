from email.policy import default
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your models here.

## MODELO DE PERFIL DEL USUARIO
SEXO_USUARIO = (
    ("1", "Masculino"),
    ("2", "Femenino"),
    ("3", "Prefiero no decirlo")
)

ESPACIO_USUARIO = (
    ("1", "Patio o Parque"),
    ("2", "Terraza o Balcon"),
    ("3", "No poseo"),
)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.PositiveIntegerField()
    sexo = models.CharField(
        max_length=30,
        choices=SEXO_USUARIO
    )
    image = models.ImageField(upload_to='posteos', null=True)
    edad = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()
    email = models.EmailField()
    localidad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=30)
    ocupacion = models.CharField(max_length=50)
    carga_horaria = models.PositiveIntegerField()
    dias_homeoffice = models.PositiveIntegerField()
    cantidad_hijos = models.PositiveIntegerField()
    cantidad_mascotas = models.PositiveIntegerField()
    especie_mascota = models.CharField(max_length=50)
    espacio_abierto = models.CharField(
        max_length=40,
        choices=ESPACIO_USUARIO
    )
    def __str__(self):
        return f'{self.user.username}: {self.first_name} {self.last_name}'

## POSTEO DE ANIMAL
ESPECIE_OPCIONES = (
    ("1", "Perro"),
    ("2", "Gato"),
)

SEXO_OPCIONES = (
    ("1", "Macho"),
    ("2", "Hembra"),
)

TAMANIO_OPCIONES = (
("1", "Grande"),
("2", "Mediano"),
("3", "Chico"),
)

CASTRACION_OPCIONES = (
    ("1", "Si"),
    ("2", "No"),
)

DESPARASITADO_OPCIONES = (
    ("1", "Si"),
    ("2", "No"),
)

#POST
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') 
    timestamp = models.DateTimeField(default=timezone.now)
    nombre = models.CharField(max_length=30, blank=True,null=True)
    especie = models.CharField(
        max_length=20,
        choices=ESPECIE_OPCIONES,
        default="Elegir Opcion"

          )
    sexo = models.CharField(
        max_length=20,
        choices=SEXO_OPCIONES, 
        default="Elegir Opcion"

    )
    edad = models.PositiveIntegerField(blank=True,null=True)
    tamanio = models.CharField(
        max_length=20,
        choices=TAMANIO_OPCIONES,
        default="Elegir Opcion"

    )
    vacunas_aplicadas = models.PositiveIntegerField(blank=True,null=True)
    castracion = models.CharField(
        max_length=20,
        choices=CASTRACION_OPCIONES, 
        default="Elegir Opcion"

    )
    desparasitado = models.CharField(
        max_length=20,
        choices=DESPARASITADO_OPCIONES,
        default="Elegir Opcion"
    )
    discapacidad = models.CharField(max_length=150, blank=True)
    content = models.TextField(max_length=500)
    imgPosteo = models.ImageField(upload_to='posteos', null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'

    
# class Avatar(models.Model):
    
   # user = models.ForeignKey(user, on_delete=models.CASCADE)
   # imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
