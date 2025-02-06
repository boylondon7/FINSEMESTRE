# Create your views here.
from django.shortcuts import render, redirect
from .models import Categorie, Produit, Client, Achat, PanierClient, Transaction, Facture

# CATEGORIES
def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'categories/liste.html', {'categories': categories})

def ajout_categorie(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        Categorie.objects.create(nom=nom)
        return redirect('liste_categories')
    return render(request, 'categories/ajout.html')

# PRODUITS
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste.html', {'produits': produits})

def ajout_produit(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prix = request.POST['prix']
        quantite = request.POST['quantite']
        description = request.POST['description']
        categorie_id = request.POST['categorie']
        categorie = Categorie.objects.get(id=categorie_id)
        Produit.objects.create(nom=nom, prix=prix, quantite=quantite, description=description, categorie=categorie)
        return redirect('liste_produits')
    categories = Categorie.objects.all()
    return render(request, 'produits/ajout.html', {'categories': categories})

# CLIENTS
def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste.html', {'clients': clients})

def ajout_client(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        contact = request.POST['contact']
        Client.objects.create(nom=nom, contact=contact)
        return redirect('liste_clients')
    return render(request, 'clients/ajout.html')

# ACHATS
def liste_achats(request):
    achats = Achat.objects.all()
    return render(request, 'achats/liste.html', {'achats': achats})

def ajout_achat(request):
    if request.method == 'POST':
        client_id = request.POST['client']
        client = Client.objects.get(id=client_id)
        Achat.objects.create(client=client, date=request.POST['date'])
        return redirect('liste_achats')
    clients = Client.objects.all()
    return render(request, 'achats/ajout.html', {'clients': clients})

# PANIERS
def liste_paniers(request):
    paniers = PanierClient.objects.all()
    return render(request, 'paniers/liste.html', {'paniers': paniers})

def ajout_panier(request):
    if request.method == 'POST':
        client_id = request.POST['client']
        produit_id = request.POST['produit']
        quantite = request.POST['quantite']
        client = Client.objects.get(id=client_id)
        produit = Produit.objects.get(id=produit_id)
        PanierClient.objects.create(client=client, produit=produit, quantite=quantite)
        return redirect('liste_paniers')
    clients = Client.objects.all()
    produits = Produit.objects.all()
    return render(request, 'paniers/ajout.html', {'clients': clients, 'produits': produits})

# TRANSACTIONS
def liste_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/liste.html', {'transactions': transactions})

def ajout_transaction(request):
    if request.method == 'POST':
        achat_id = request.POST['achat']
        montant = request.POST['montant']
        type_paiement = request.POST['type_paiement']
        achat = Achat.objects.get(id=achat_id)
        Transaction.objects.create(achat=achat, montant=montant, type_paiement=type_paiement)
        return redirect('liste_transactions')
    achats = Achat.objects.all()
    return render(request, 'transactions/ajout.html', {'achats': achats})

# FACTURES
def liste_factures(request):
    factures = Facture.objects.all()
    return render(request, 'factures/liste.html', {'factures': factures})

def ajout_facture(request):
    if request.method == 'POST':
        achat_id = request.POST['achat']
        date = request.POST['date']
        total = request.POST['total']
        achat = Achat.objects.get(id=achat_id)
        Facture.objects.create(achat=achat, date=date, total=total)
        return redirect('liste_factures')
    achats = Achat.objects.all()
    return render(request, 'factures/ajout.html', {'achats': achats})
#Index
def index(request):
    return render(request, 'index.html')