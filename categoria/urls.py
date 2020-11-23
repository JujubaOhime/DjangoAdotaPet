from django.urls import path

from categoria import views

app_name = 'categoria'

urlpatterns = [
    path('cadastra_categoria/', views.cadastra_categoria, name='cadastra_categoria'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('exibe_categoria/<int:id>', views.exibe_categoria, name='exibe_categoria'),
    path('edita_categoria/<int:id>', views.edita_categoria, name='edita_categoria'),
    path('remove_categoria/<int:id>', views.remove_categoria, name='remove_categoria')


]