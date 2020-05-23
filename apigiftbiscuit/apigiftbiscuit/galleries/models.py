from django.db import models


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome:', max_length=35)
    description_short = models.CharField('Descrição curta:', max_length=50)
    cover_image = models.ImageField('Imagem de capa:', max_length=255, upload_to='albums')
    slug = models.SlugField('Identificador:', max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Álbum'
        verbose_name_plural = 'Álbums'
        ordering = ['-id']

    def __str__(self):
        return self.name    


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField('Foto:', upload_to='photos')
    description_short = models.CharField('Descrição curta:', max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['-id']

    def __str__(self):
        return self.photo
