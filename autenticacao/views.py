from django.shortcuts import render, redirect

from autenticacao.forms import UsuarioFormCustomizado, ProfileForm


def registra_usuario(request):
    if request.method == 'POST':
        form = UsuarioFormCustomizado(request.POST)
        u_form = ProfileForm(request.POST)


        if form.is_valid() and u_form.is_valid():
            form.save()
            u_form.save()
            form = UsuarioFormCustomizado()
            u_form = ProfileForm()
                
    else:
        form = UsuarioFormCustomizado()
        u_form = ProfileForm()

    context={
        'form': form, 'u_form': u_form 
    }

    return render(request, 'autenticacao/registra_usuario.html', context)

def exibe_usuario(request):
    pass

