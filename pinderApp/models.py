from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='user.png')

    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'


##POST
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') 
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=500)
    imgPosteo = models.ImageField(upload_to='posteos', null=True)


    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'
