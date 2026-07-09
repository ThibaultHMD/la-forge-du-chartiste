from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    couverture_url = models.URLField(blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} — {self.auteur}"
