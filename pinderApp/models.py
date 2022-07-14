from django.db import models

# Create your models here.

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
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.PositiveIntegerField()
    sexo = models.CharField(
        max_length=30,
        choices=SEXO_USUARIO
    )
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


class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    especie = models.CharField(
        max_length=20,
        choices=ESPECIE_OPCIONES,
          )
    sexo = models.CharField(
        max_length=20,
        choices=SEXO_OPCIONES, 
    )
    foto = models.CharField(max_length=9999999)
    edad = models.PositiveIntegerField()
    tamanio = models.CharField(
        max_length=20,
        choices=TAMANIO_OPCIONES,
    )
    vacunas_aplicadas = models.PositiveIntegerField()
    castracion = models.CharField(
        max_length=20,
        choices=CASTRACION_OPCIONES, 
    )
    desparasitado = models.CharField(
        max_length=20,
        choices=DESPARASITADO_OPCIONES,
    )
    discapacidad = models.CharField(max_length=150)


# class Publicacion(models.Model):
  # title = models.CharField(max_length=200, verbose_name="Título")
  # content = models.TextField(verbose_name="Contenido")
  # published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
  # image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
  # author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
  # categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
  # created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  # updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

  #  class Meta:
      # verbose_name = "entrada"
      # verbose_name_plural = "entradas"
      # ordering = ['-created']

  #  def __str__(self):
      #  return self.title


# class Avatar(models.Model):
    
   # user = models.ForeignKey(user, on_delete=models.CASCADE)
   # imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

