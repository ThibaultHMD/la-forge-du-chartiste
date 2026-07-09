from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_livres, name='liste_livres'),
]