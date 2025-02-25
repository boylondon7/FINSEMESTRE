#Date: 09/02/2025
#Auteur :GAGALO Livingstone
#But: Projet de fin de semestre



from django.urls import path
from . import views

urlpatterns = [

    #Accueil
    #url pour la page d'accueil
    path('', views.index, name="index"), 
    # CATEGORIES
        #url pour l'affichage de la liste des categories
    path('categories/', views.liste_categories, name="liste_categories"),
        #url pour l'ajout d'une nouvelle categorie
    path('categories/nouveau/', views.ajout_categorie, name="ajout_categorie"),
        #url pour la modification d'une categorie
    path('categories/modifier/<int:pk>/', views.modifier_categorie, name='modifier_categorie'),
        #url pour la suppression d'une categorie
    path('categories/supprimer/<int:pk>/', views.supprimer_categorie, name='supprimer_categorie'),

    # PRODUITS
        #Url d'affichage des produits
    path('produits/', views.liste_produits, name="liste_produits"),
        #url d'ajout d'un nouveau produit
    path('produits/nouveau/', views.ajout_produit, name="ajout_produit"),
        #url de modification d'un produit
    path('produits/modifier/<int:pk>/', views.modifier_produit, name='modifier_produit'),
        #url de suppression d'un produit
    path('produits/supprimer/<int:pk>/', views.supprimer_produit, name='supprimer_produit'),

    # CLIENTS
        #url d'affichage des clients
    path('clients/', views.liste_clients, name="liste_clients"),
        #url d'ajout d'un nouveau client
    path('clients/nouveau/', views.ajout_client, name="ajout_client"),
        #url de modification d'un client
    path('clients/modifier/<int:pk>/', views.modifier_client, name='modifier_client'),
        #url de suppression d'un client
    path('clients/supprimer/<int:pk>/', views.supprimer_client, name='supprimer_client'),

    # ACHATS
        #url d'affichage des achats
    path('achats/', views.liste_achats, name="liste_achats"),
        #url d'ajout d'un nouveau achat
    path('achats/nouveau/', views.ajout_achat, name="ajout_achat"),
        #url de modification d'un achat
    path('achats/modifier/<int:pk>/', views.modifier_achat, name='modifier_achat'),
        #url de suppression d'un achat
    path('achats/supprimer/<int:pk>/', views.supprimer_achat, name='supprimer_achat'),

    # PANIERS
        #url d'affichage des paniers
    path('panier/', views.liste_paniers, name="liste_paniers"),
        #url d'ajout d'un nouveau panier
    path('panier/ajout/', views.ajout_panier, name="ajout_panier"),
        #url de modification d'un panier
    path('panier/modifier/<int:pk>/', views.modifier_panier, name='modifier_panier'),
        #url de suppression d'un panier
    path('panier/supprimer/<int:pk>/', views.supprimer_panier, name='supprimer_panier'),

    # TRANSACTIONS
        #url d'affichage des transactions
    path('transactions/', views.liste_transactions, name="liste_transactions"),
        #url d'ajout d'une nouvelle transaction
    path('transactions/nouveau/', views.ajout_transaction, name="ajout_transaction"),
        #url de modification d'une transaction
    path('transactions/modifier/<int:pk>/', views.modifier_transaction, name='modifier_transaction'),
         #url de suppression d'une transaction
    path('transactions/supprimer/<int:pk>/', views.supprimer_transaction, name='supprimer_transaction'),
    

    # FACTURES
        #url d'affichage des factures
    path('factures/', views.liste_factures, name="liste_factures"),
        #url d'ajout d'une nouvelle facture
    path('factures/nouveau/', views.ajout_facture, name="ajout_facture"),
    

         


]
