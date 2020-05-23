from django.db import models


class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome:', max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Budget(models.Model):
    id = models.AutoField(primary_key=True)
    categorie = models.ForeignKey(Categorie, null=True, related_name='budgets', on_delete=models.CASCADE)
    name = models.CharField('Nome completo:', max_length=50)
    email = models.EmailField('Email de contato:', max_length=40)
    phone = models.CharField('Telefone de contato:', max_length=14)
    description = models.TextField('Descrição:')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['-id']

    def __str__(self):
        return self.name
