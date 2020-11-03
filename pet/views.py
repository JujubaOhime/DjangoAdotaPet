from django.shortcuts import render

def index(request):
    frase = "esta frase está sendo exibida pela página index.html de pet"
    return render(request, 'pet/index.html', {'frase': frase})

def lista_pets(request):
    pass

def pagina1(request):
    frase = "esta frase está sendo exibida pela página pagina1.html de pet"
    return render(request, 'pet/pagina1.html', {'frase': frase})

def pagina2(request):
    frase = "esta frase está sendo exibida pela página pagina2.html de pet"
    return render(request, 'pet/pagina2.html', {'frase': frase})