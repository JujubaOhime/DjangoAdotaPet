from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
import datetime

class PetOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genero_escolhas = [('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Outro')]
    genero = models.CharField(max_length=1, choices=genero_escolhas, default='N')
    imagem = models.CharField(max_length=50, blank=True)
    data_cadastro = models.DateField(default=datetime.date.today)
    data_nascimento = models.DateField()
    estado_escolhas = [('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
                       ('BA', 'Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
                       ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
                       ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
                       ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
                       ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
                       ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
                       ('SP', 'São Paulo'), ('SE', 'Sergipe'),
                       ('TO', 'Tocantins'), ('DF', 'Distrito Federal')]

    estado = models.CharField(max_length=2, choices=estado_escolhas)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=20)
    link_instagram = models.URLField(max_length=200, blank=True)
    link_facebook = models.URLField(max_length=200, blank=True)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=12)


