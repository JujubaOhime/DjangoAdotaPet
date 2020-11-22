from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime

from autenticacao.models import Profile
from categoria.models import Categoria

class Pet(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='pets', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100)
    imagem = models.CharField(max_length=50, blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2, default="0,00")
    disponivel = models.BooleanField(default=False)
    link_instagram = models.URLField(max_length=200, blank=True)
    link_facebook = models.URLField(max_length=200, blank=True)
    telefone = models.CharField(max_length=15)
    sexo_escolhas = [('F', 'Fêmea'), ('M', 'Macho'), ('N', 'Não sei')]
    sexo = models.CharField(max_length=1, choices=sexo_escolhas, default='N')
    descricao = models.TextField()
    data_cadastro = models.DateField(default=datetime.now)
    data_nascimento = models.DateField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    raca = models.CharField(max_length=20, blank=True)
    estado_escolhas = [('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
                       ('BA', 'Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
                       ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
                       ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
                       ('PE', 'Pernambuco'),('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
                       ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
                       ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
                       ('SP', 'São Paulo'), ('SE', 'Sergipe'),
                       ('TO', 'Tocantins'), ('DF', 'Distrito Federal')]

    estado = models.CharField(max_length=2, choices=estado_escolhas)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    class Meta:
        db_table='pet'

    def __str__(self):
        return self.nome

    def get_sexo(self):
        if self.sexo == "M":
            return "Macho"
        elif self.sexo == "F":
            return "Fêmea"
        elif self.sexo == "N":
            return "Não sabe"

    def get_disponivel(self):
        if self.disponivel:
            return "Sim"
        else:
            return "Não"

    def get_meses(self):
        pass
