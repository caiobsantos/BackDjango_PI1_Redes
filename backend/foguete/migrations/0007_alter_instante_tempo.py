# Generated by Django 4.2.7 on 2023-12-14 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foguete', '0006_alter_instante_idinstante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instante',
            name='tempo',
            field=models.IntegerField(),
        ),
    ]