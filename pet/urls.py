from django.urls import path

from pet import views

app_name = 'pet'

urlpatterns = [
    path('', views.index, name='index'),
    path('paginas/pagina1/', views.pagina1, name='pagina1'),
    path('paginas/pagina2/', views.pagina2, name='pagina2'),
]