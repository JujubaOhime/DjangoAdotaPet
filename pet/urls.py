from django.urls import path

from pet import views

app_name = 'pet'

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_pets/', views.lista_pets, name='lista_pets'),
    path('cadastra_pets/', views.cadastra_pets, name='cadastra_pets'),
    path('exibe_pet/<int:id>', views.exibe_pet, name='exibe_pet')
]