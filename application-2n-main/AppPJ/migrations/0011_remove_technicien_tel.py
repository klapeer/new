# Generated by Django 4.0.3 on 2022-07-18 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPJ', '0010_alter_technicien_tel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicien',
            name='tel',
        ),
    ]