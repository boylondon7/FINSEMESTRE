from django.urls import path
from . import views

urlpatterns = [

    #Accueil
    path('', views.index, name="index"), 
    # CATEGORIES
    path('categories/', views.liste_categories, name="liste_categories"),
    path('categories/nouveau/', views.ajout_categorie, name="ajout_categorie"),
    path('categories/modifier/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/', views.supprimer_categorie, name='supprimer_categorie'),

    # PRODUITS
    path('produits/', views.liste_produits, name="liste_produits"),
    path('produits/nouveau/', views.ajout_produit, name="ajout_produit"),
    path('produits/modifier/', views.modifier_produit, name='modifier_produit'),
    path('produits/supprimer/', views.supprimer_produit, name='supprimer_produit'),

    # CLIENTS
    path('clients/', views.liste_clients, name="liste_clients"),
    path('clients/nouveau/', views.ajout_client, name="ajout_client"),
    path('clients/modifier/', views.modifier_client, name='modifier_client'),
    path('clients/supprimer/', views.supprimer_client, name='supprimer_client'),

    # ACHATS
    path('achats/', views.liste_achats, name="liste_achats"),
    path('achats/nouveau/', views.ajout_achat, name="ajout_achat"),
    path('achats/modifier/', views.modifier_achat, name='modifier_achat'),
    path('achats/supprimer/', views.supprimer_achat, name='supprimer_achat'),

    # PANIERS
    path('panier/', views.liste_paniers, name="liste_paniers"),
    path('panier/ajout/', views.ajout_panier, name="ajout_panier"),
    path('panier/modifier/', views.modifier_panier, name='modifier_panier'),
    path('panier/supprimer/', views.supprimer_panier, name='supprimer_panier'),

    # TRANSACTIONS
    path('transactions/', views.liste_transactions, name="liste_transactions"),
    path('transactions/nouveau/', views.ajout_transaction, name="ajout_transaction"),
    path('transactions/modifier/', views.modifier_transaction, name='modifier_transaction'),
    path('transactions/supprimer/', views.supprimer_transaction, name='supprimer_transaction'),
    

    # FACTURES
    path('factures/', views.liste_factures, name="liste_factures"),
    path('factures/nouveau/', views.ajout_facture, name="ajout_facture"),


]
