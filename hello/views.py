from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return HttpResponse('Hello World!')


def turma_page_view(request):
    return HttpResponse('Olá turma!')


def sauda_page_view(request, name):
    return HttpResponse(f'Olá, {name.capitalize()} 😀!')