from pyexpat.errors import messages

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from autenticacao.forms import UsuarioFormCustomizado, ProfileForm


def registra_usuario(request):
    if request.method == 'POST':
        form = UsuarioFormCustomizado(request.POST)
        u_form = ProfileForm(request.POST)


        if form.is_valid() and u_form.is_valid():
            user = form.save()
            profile = u_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

        else:
            print("ué")
            print(form.errors)
            print(u_form.errors)
            ctx = {'form': form, 'u_form': u_form}
            return render(request, 'autenticacao/registra_usuario.html', ctx)
                
    else:
        form = UsuarioFormCustomizado()
        u_form = ProfileForm()

    context = {
        'form': form, 'u_form': u_form 
    }

    return render(request, 'autenticacao/registra_usuario.html', {'form': form, 'u_form': u_form})

def exibe_usuario(request):
    pass

