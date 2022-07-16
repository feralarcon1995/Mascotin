from django import forms


class Animal(forms.Form):
    
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

    nombre = forms.CharField(max_length=30)
    especie = forms.ChoiceField(choices=ESPECIE_OPCIONES)
    sexo = forms.ChoiceField(choices=SEXO_OPCIONES)
    foto = forms.CharField(max_length=9999999)
    edad = forms.PositiveIntegerField()
    tamanio = forms.ChoiceField(choices=TAMANIO_OPCIONES)
    vacunas_aplicadas = forms.PositiveIntegerField()
    castracion = forms.ChoiceField(choices=CASTRACION_OPCIONES)
    desparasitado = forms.ChoiceField(choices=DESPARASITADO_OPCIONES)
    discapacidad = forms.CharField(max_length=150)


class Usuario(forms.Form):
    
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

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.PositiveIntegerField()
    sexo = forms.ChoiceField(choices=SEXO_USUARIO)
    edad = forms.PositiveIntegerField()
    telefono = forms.PositiveIntegerField()
    email = forms.EmailField()
    localidad = forms.CharField(max_length=50)
    provincia = forms.CharField(max_length=30)
    ocupacion = forms.CharField(max_length=50)
    carga_horaria = forms.PositiveIntegerField()
    dias_homeoffice = forms.PositiveIntegerField()
    cantidad_hijos = forms.PositiveIntegerField()
    cantidad_mascotas = forms.PositiveIntegerField()
    especie_mascota = forms.CharField(max_length=50)
    espacio_abierto = forms.ChoiceField(choices=ESPACIO_USUARIO)

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