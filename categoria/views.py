from django.conf.urls import url
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from categoria.forms import PesquisaCategoriaForm, CategoriaForm
from categoria.models import Categoria
from django.template.defaultfilters import slugify
from django.contrib import messages


@user_passes_test(lambda u: u.is_staff)
def lista_categorias(request):
    form = PesquisaCategoriaForm(request.GET)
    if form.is_valid():
        query_string = form.cleaned_data['query_string']
        lista_de_categorias = Categoria.objects.filter(nome__icontains=query_string).order_by('nome')
        paginator = Paginator(lista_de_categorias, 7)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)

        print(lista_de_categorias)
        print(page_obj)

        return render(request, 'categoria/pesquisa_categoria.html', {'categorias': page_obj, 'form': form, 'query_string': query_string})
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentar recuperar a categoria.")

@user_passes_test(lambda u: u.is_staff)
def cadastra_categoria(request):

    if request.POST:
        categoria_id = request.session.get('categoria_id')
        print('categoria_id na sessão = ' + str(categoria_id))
        if categoria_id:
            categoria = get_object_or_404(Categoria, pk=categoria_id)
            categoria_form = CategoriaForm(request.POST, instance=categoria)
        else:
            categoria_form = CategoriaForm(request.POST)

        if categoria_form.is_valid():

            categoria = categoria_form.save(commit=False)
            categoria.slug = slugify(categoria.nome)
            categoria.save()

            if categoria_id:
                messages.add_message(request, messages.INFO, 'Categoria alterado com sucesso!')
                del request.session['categoria_id']
            else:
                messages.add_message(request, messages.INFO, 'Categoria cadastrada com sucesso!')

            return HttpResponseRedirect(reverse('categoria:lista_categorias'))

        else:
            print("ué")
            print(categoria_form.errors)
            ctx = {'categoria_form': categoria_form}
            return render(request, 'categoria/cadastra_categoria.html', ctx)

    else:
        try:
            del request.session['categoria_id']
        except KeyError:
            pass
        categoria_form = CategoriaForm()

    return render(request, 'categoria/cadastra_categoria.html', {'form': categoria_form})

@user_passes_test(lambda u: u.is_staff)
def edita_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    categoria_form = CategoriaForm(instance=categoria)
    request.session['categoria_id'] = id
    return render(request, 'categoria/cadastra_categoria.html', {'form': categoria_form})

@user_passes_test(lambda u: u.is_staff)
def exibe_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    return render(request, 'categoria/exibe_categoria.html', {'categoria': categoria})

@user_passes_test(lambda u: u.is_staff)
def remove_categoria(request, id):
    obj = get_object_or_404(Categoria, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('categoria:lista_categorias'))
    context = {
        'object': obj
    }
    return render(request, 'categoria/pesquisa_categoria.html', context)