# Generated by Django 3.1.2 on 2020-11-02 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_auto_20201102_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='sexo',
            field=models.CharField(choices=[('F', 'Fêmea'), ('M', 'Macho'), ('N', 'Não sei')], default='N', max_length=1),
        ),
    ]