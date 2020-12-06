# Generated by Django 3.1.2 on 2020-12-05 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('pet', '0005_auto_20201205_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pets', to='categoria.categoria'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='cep',
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AlterField(
            model_name='pet',
            name='cidade',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='pet',
            name='estado',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('DF', 'Distrito Federal')], max_length=2),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Fêmea'), ('M', 'Macho'), ('N', 'Não sei')], default='N', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='telefone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
