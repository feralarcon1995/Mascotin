# Generated by Django 4.0.5 on 2022-07-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinderApp', '0011_alter_usuario_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(null=True, upload_to='posteos'),
        ),
    ]