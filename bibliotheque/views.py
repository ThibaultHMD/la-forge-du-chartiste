from django.shortcuts import render
from .models import Livre

def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres})
