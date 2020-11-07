from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from pet.forms import PesquisaPetForm, PetForm
from pet.models import Pet
from django.template.defaultfilters import slugify


@user_passes_test(lambda u: u.is_staff)
def index(request):
    frase = "esta frase está sendo exibida pela página index.html de pet"
    return render(request, 'pet/index.html', {'frase': frase})

@user_passes_test(lambda u: u.is_staff)
def lista_pets(request):
    form = PesquisaPetForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_pets = Pet.objects.filter(nome__icontains=nome).order_by('nome')
        paginator = Paginator(lista_de_pets, 3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)

        print(lista_de_pets)
        print(page_obj)

        return render(request, 'pet/pesquisa_pet.html', {'pets': page_obj, 'form': form, 'nome': nome})
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentr recuperar pet.")

@user_passes_test(lambda u: u.is_staff)
def cadastra_pets(request):
    pet_form = PetForm()

    return render(request, 'pet/cadastra_pet.html', {'form': pet_form})

@user_passes_test(lambda u: u.is_staff)
def exibe_pet(request, id):
    pet = get_object_or_404(Pet, pk=id)
    request.session['pet_id_del'] = id
    return render(request, 'pet/exibe_produto.html', {'pet': pet})

@user_passes_test(lambda u: u.is_staff)
def edita_pet(request, id):
    pet = get_object_or_404(Pet, pk=id)
    pet_form = PetForm(instance=pet)
    request.session['pet_id'] = id
    return render(request, 'pet/cadastra_pet.html', {'form': pet_form})