# Generated by Django 3.1.2 on 2020-11-02 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('pet', '0002_auto_20201102_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pets', to='categoria.categoria'),
        ),
    ]