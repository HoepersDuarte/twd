from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Hellow Word!'
    context_dict['autor'] = 'HoepersDuarte'
    return render(request, 'rango/inde.html', context=context_dict)


def about(request):
    texto = '''
    <h1> Sobre o Rango </h1>
    Essa é a página sobre o Rango.

    <br/><a href='/rango/'>Index</a>
    '''
    return HttpResponse(texto)

