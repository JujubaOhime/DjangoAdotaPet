from django.shortcuts import render


def index(request):
    frase = 'Esta frase está sendo exibida pela página index.html'
    return render(request, 'index.html', {'frase': frase})

def about(request):
    frase = 'Esta frase está sendo exibida pela página about.html'
    return render(request, 'about.html', {'frase': frase})