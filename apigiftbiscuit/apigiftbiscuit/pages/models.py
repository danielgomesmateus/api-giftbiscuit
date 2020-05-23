from django.db import models


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título:', max_length=35)
    content = models.TextField('Conteúdo:')
    slug = models.SlugField('Identificador:', max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['-id']

    def __str__(self):
        return self.title
