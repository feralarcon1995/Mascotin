# Generated by Django 4.0.5 on 2022-07-16 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinderApp', '0017_rename_user_post_usuario_rename_user_usuario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
    ]
