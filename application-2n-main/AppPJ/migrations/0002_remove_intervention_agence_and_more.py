# Generated by Django 4.0.3 on 2022-06-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPJ', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intervention',
            name='agence',
        ),
        migrations.RemoveField(
            model_name='intervention',
            name='type_logiciel',
        ),
        migrations.RemoveField(
            model_name='intervention',
            name='type_materiel',
        ),
        migrations.RemoveField(
            model_name='panne',
            name='agence',
        ),
        migrations.AlterField(
            model_name='intervention',
            name='cout_de_reparation',
            field=models.IntegerField(help_text='veiller remplir'),
        ),
        migrations.AlterField(
            model_name='panne',
            name='description_panne',
            field=models.TextField(help_text='veiller remplir'),
        ),
    ]
