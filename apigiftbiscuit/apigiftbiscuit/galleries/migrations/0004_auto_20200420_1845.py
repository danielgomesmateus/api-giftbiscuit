# Generated by Django 3.0.4 on 2020-04-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_album_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_image',
            field=models.ImageField(max_length=255, upload_to='albuns', verbose_name='Imagem de capa:'),
        ),
    ]
