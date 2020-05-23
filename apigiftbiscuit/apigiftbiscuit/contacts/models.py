from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome completo:', max_length=50)
    email = models.EmailField('Email de contato:', max_length=40)
    phone = models.CharField('Telefone de contato:', max_length=14)
    message = models.TextField('Mensagem:')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['-id']

    def __str__(self):
        return self.name

