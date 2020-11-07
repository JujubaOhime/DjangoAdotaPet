from django.shortcuts import render, redirect

from autenticacao.forms import UsuarioFormCustomizado, ProfileForm


def registra_usuario(request):
    if request.method == 'POST':
        form = UsuarioFormCustomizado(request.POST)
        u_form = ProfileForm(request.POST)


        if form.is_valid() and u_form.is_valid():
            pass
    else:
        form = UsuarioFormCustomizado()
        u_form = ProfileForm()

    return render(request, 'autenticacao/registra_usuario.html', {'form': form, 'u_form': u_form})

def exibe_usuario(request):
    pass

