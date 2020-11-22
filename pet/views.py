from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from pet.forms import PesquisaPetForm, PetForm
from pet.models import Pet
from django.template.defaultfilters import slugify
from django.contrib import messages


def index(request):
    form = PesquisaPetForm(request.GET)
    if form.is_valid():
        query_string = form.cleaned_data['query_string']
        lista_de_pets = Pet.objects.filter(nome__icontains=query_string).order_by('nome') | Pet.objects.filter(cidade__icontains=query_string).order_by('nome') | Pet.objects.filter(estado__icontains=query_string).order_by('nome')
        paginator = Paginator(lista_de_pets, 3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)

        print(lista_de_pets)
        print(page_obj)

        return render(request, 'pet/index.html', {'pets': page_obj, 'form': form, 'query_string': query_string})
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentr recuperar pet.")

@user_passes_test(lambda u: u.is_staff)
def lista_pets(request):
    form = PesquisaPetForm(request.GET)
    if form.is_valid():
        query_string = form.cleaned_data['query_string']
        lista_de_pets = Pet.objects.filter(nome__icontains=query_string).order_by('nome') | Pet.objects.filter(cidade__icontains=query_string).order_by('nome') | Pet.objects.filter(estado__icontains=query_string).order_by('nome') 
        paginator = Paginator(lista_de_pets, 3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)

        print(lista_de_pets)
        print(page_obj)

        return render(request, 'pet/pesquisa_pet.html', {'pets': page_obj, 'form': form, 'query_string': query_string})
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentr recuperar pet.")

@user_passes_test(lambda u: u.is_staff)
def cadastra_pets(request):

    if request.POST:
        pet_form = PetForm(request.POST)
        if pet_form.is_valid():
            pet = pet_form.save(commit=False)
            pet.slug = slugify(pet.nome)
            pet.usuario = request.user
            pet.save()
            messages.add_message(request, messages.INFO, 'Pet cadastrado com sucesso!')

            return render(request, 'pet/exibe_pet.html', {'pet': pet})

        else:
            print("ué")
            print(pet_form.errors)
            ctx = {'pet_form': pet_form}
            return render(request, 'autenticacao/cadastra_pet.html', ctx)

    else:
        pet_form = PetForm()

    return render(request, 'pet/cadastra_pet.html', {'form': pet_form})


def exibe_pet(request, id):
    pet = get_object_or_404(Pet, pk=id)
    request.session['pet_id_del'] = id
    return render(request, 'pet/exibe_pet.html', {'pet': pet})

@user_passes_test(lambda u: u.is_staff)
def edita_pet(request, id):
    pet = get_object_or_404(Pet, pk=id)
    pet_form = PetForm(instance=pet)
    request.session['pet_id'] = id
    return render(request, 'pet/cadastra_pet.html', {'form': pet_form})