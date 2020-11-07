from django.contrib.auth import views as auth_views
from django.urls import path
from autenticacao import views
from autenticacao.forms import AuthenticationFormCustomizado

app_name = 'autenticacao'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form = AuthenticationFormCustomizado,
                                                template_name='autenticacao/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registra_usuario/', views.registra_usuario, name='registra_usuario'),
    path('exibe_usuario/', views.exibe_usuario, name='exibe_usuario'),
]
