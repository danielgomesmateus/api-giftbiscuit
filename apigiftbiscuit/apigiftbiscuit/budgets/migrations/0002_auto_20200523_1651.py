# Generated by Django 3.0.4 on 2020-05-23 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to='budgets.Categorie'),
        ),
    ]
