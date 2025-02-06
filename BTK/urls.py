from django.urls import path
from . import views

urlpatterns = [
    # CATEGORIES
    path('categories/', views.liste_categories, name="liste_categories"),
    path('categories/nouveau/', views.ajout_categorie, name="ajout_categorie"),

    # PRODUITS
    path('produits/', views.liste_produits, name="liste_produits"),
    path('produits/nouveau/', views.ajout_produit, name="ajout_produit"),

    # CLIENTS
    path('clients/', views.liste_clients, name="liste_clients"),
    path('clients/nouveau/', views.ajout_client, name="ajout_client"),

    # ACHATS
    path('achats/', views.liste_achats, name="liste_achats"),
    path('achats/nouveau/', views.ajout_achat, name="ajout_achat"),

    # PANIERS
    path('panier/', views.liste_paniers, name="liste_paniers"),
    path('panier/ajout/', views.ajout_panier, name="ajout_panier"),

    # TRANSACTIONS
    path('transactions/', views.liste_transactions, name="liste_transactions"),
    path('transactions/nouveau/', views.ajout_transaction, name="ajout_transaction"),

    # FACTURES
    path('factures/', views.liste_factures, name="liste_factures"),
    path('factures/nouveau/', views.ajout_facture, name="ajout_facture"),
]
