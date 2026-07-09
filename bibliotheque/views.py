from django.shortcuts import render, redirect
from .models import Livre
from .services import recuperer_infos_isbn

def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres})

def ajouter_livre(request):
    if request.method == "POST":
        isbn = request.POST.get("isbn")
        infos = recuperer_infos_isbn(isbn)

        if infos:
            Livre.objects.create(
                titre=infos["titre"],
                auteur=infos["auteur"],
                isbn=isbn,
                couverture_url=infos["couverture_url"],
            )
            return redirect("liste_livres")
        else:
            return render(request, "bibliotheque/ajouter_livre.html", {
                "erreur": "ISBN introuvable, vérifie le numéro."
            })

    return render(request, "bibliotheque/ajouter_livre.html")
