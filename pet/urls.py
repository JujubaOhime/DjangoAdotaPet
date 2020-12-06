from django.urls import path

from pet import views

app_name = 'pet'

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_pets/', views.lista_pets, name='lista_pets'),
    path('cadastra_pets/', views.cadastra_pets, name='cadastra_pets'),
    path('exibe_pet/<int:id>', views.exibe_pet, name='exibe_pet'),
    path('edita_pet/<int:id>', views.edita_pet, name='edita_pet'),
    path('remove_pet/<int:id>', views.remove_pet, name='remove_pet'),

    path('ajax_pet/', views.ajax_pet, name='ajax_pet'),
    path('ajax_pet/<int:id>', views.ajax_pet_delete, name='ajax_pet_delete'),
]