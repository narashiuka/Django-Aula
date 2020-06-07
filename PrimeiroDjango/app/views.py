"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def hello(request, nome, idade):
    return HttpResponse(f"<h1>Hello {nome}, você tem {idade} anos!</h1>")

def soma(request, num1, num2):
    somando = num1 + num2
    return HttpResponse(f"A soma do primeiro numero {num1} mais o segundo {num2} é: {somando}")

def subtracao(request, num1, num2):
    menos = num1 - num2
    return HttpResponse(f"A subtração do primeiro numero {num1} menos o segundo {num2} é: {menos}")

def multiplicacao(request, num1, num2):
    multi = num1 * num2
    return HttpResponse(f"A multiplicação do primeiro numero {num1} vezes o segundo {num2} é: {multi}")

def divisao(request, num1, num2):
    div = num1 / num2
    return HttpResponse(f"A divisão do primeiro numero {num1} pelo segundo {num2} é: {div}")