from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("HOME")

def contato(request):
    return render(request, 'recipes/home.html', context={'nome': 'Joao Victor'}) # django ja busca na pasta templates