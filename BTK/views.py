from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Categorie, Produit, Client, Achat, PanierClient, Transaction, Facture

# CATEGORIES
def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'categories/liste.html', {'categories': categories})

def ajout_categorie(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        Categorie.objects.create(nom=nom)
        return HttpResponseRedirect('/categories/')
    return render(request, 'categories/ajout.html')

def modifier_categorie(request, pk):
    categorie = Categorie.objects.get(pk=pk)
    if request.method == 'POST':
        categorie.nom = request.POST['nom']
        categorie.save()
        return HttpResponseRedirect('/categories/')
    return render(request, 'categories/modifier.html', {'categorie': categorie})

def supprimer_categorie(request, pk):
    categorie = Categorie.objects.get(pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return HttpResponseRedirect('/categories/')
    return render(request, 'categories/supprimer.html', {'categorie': categorie})

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
        return HttpResponseRedirect('/produits/')
    categories = Categorie.objects.all()
    return render(request, 'produits/ajout.html', {'categories': categories})

def modifier_produit(request, pk):
    produit = Produit.objects.get(pk=pk)
    if request.method == 'POST':
        produit.nom = request.POST['nom']
        produit.prix = request.POST['prix'] 
        produit.quantite = request.POST['quantite']
        produit.description = request.POST['description']
        produit.categorie = Categorie.objects.get(id=request.POST['categorie'])
        produit.save()
        return HttpResponseRedirect('/produits/')
    categories = Categorie.objects.all()
    return render(request, 'produits/modifier.html', {'produit': produit, 'categories': categories})

def supprimer_produit(request, pk):
    produit = Produit.objects.get(pk=pk)
    if request.method == 'POST':
        produit.delete()
        return HttpResponseRedirect('/produits/')
    return render(request, 'produits/supprimer.html', {'produit': produit})

# CLIENTS
def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste.html', {'clients': clients})

def ajout_client(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        contact = request.POST['contact']
        Client.objects.create(nom=nom, contact=contact)
        return HttpResponseRedirect('/clients/')
    return render(request, 'clients/ajout.html')

def modifier_client(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        client.nom = request.POST['nom']
        client.contact = request.POST['contact']
        client.save()
        return HttpResponseRedirect('/clients/')
    return render(request, 'clients/modifier.html', {'client': client})

def supprimer_client(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        client.delete()
        return HttpResponseRedirect('/clients/')
    return render(request, 'clients/supprimer.html', {'client': client})

# ACHATS
def liste_achats(request):
    achats = Achat.objects.all()
    return render(request, 'achats/liste.html', {'achats': achats})

def ajout_achat(request):
    if request.method == 'POST':
        client = Client.objects.get(id=request.POST['client'])
        Achat.objects.create(client=client, date=request.POST['date'])
        return HttpResponseRedirect('/achats/')
    clients = Client.objects.all()
    return render(request, 'achats/ajout.html', {'clients': clients})

def modifier_achat(request, pk):
    achat = Achat.objects.get(pk=pk)
    if request.method == 'POST':
        achat.client = Client.objects.get(id=request.POST['client'])
        achat.date = request.POST['date']
        achat.save()
        return HttpResponseRedirect('/achats/')
    clients = Client.objects.all()
    return render(request, 'achats/modifier.html', {'achat': achat, 'clients': clients})

def supprimer_achat(request, pk):
    achat = Achat.objects.get(pk=pk)
    if request.method == 'POST':
        achat.delete()
        return HttpResponseRedirect('/achats/')
    return render(request, 'achats/supprimer.html', {'achat': achat})

# PANIERS
def liste_paniers(request):
    paniers = PanierClient.objects.all()
    return render(request, 'paniers/liste.html', {'paniers': paniers})

def ajout_panier(request):
    if request.method == 'POST':
        client = Client.objects.get(id=request.POST['client'])
        produit = Produit.objects.get(id=request.POST['produit'])
        PanierClient.objects.create(client=client, produit=produit, quantite=request.POST['quantite'])
        return HttpResponseRedirect('/paniers/')
    clients = Client.objects.all()
    produits = Produit.objects.all()
    return render(request, 'paniers/ajout.html', {'clients': clients, 'produits': produits})

def modifier_panier(request, pk):
    panier = PanierClient.objects.get(pk=pk)
    if request.method == 'POST':
        panier.client = Client.objects.get(id=request.POST['client'])
        panier.produit = Produit.objects.get(id=request.POST['produit'])
        panier.quantite = request.POST['quantite']
        panier.save()
        return HttpResponseRedirect('/paniers/')
    clients = Client.objects.all()
    produits = Produit.objects.all()
    return render(request, 'paniers/modifier.html', {'panier': panier, 'clients': clients, 'produits': produits})

def supprimer_panier(request, pk):
    panier = PanierClient.objects.get(pk=pk)
    if request.method == 'POST':
        panier.delete()
        return HttpResponseRedirect('/paniers/')
    return render(request, 'paniers/supprimer.html', {'panier': panier})

# TRANSACTIONS
def liste_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/liste.html', {'transactions': transactions})

def ajout_transaction(request):
    if request.method == 'POST':
        achat = Achat.objects.get(id=request.POST['achat'])
        Transaction.objects.create(
            achat=achat,
            montant=request.POST['montant'],
            type_paiement=request.POST['type_paiement']
        )
        return HttpResponseRedirect('/transactions/')
    achats = Achat.objects.all()
    return render(request, 'transactions/ajout.html', {'achats': achats})

def modifier_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.achat = Achat.objects.get(id=request.POST['achat'])
        transaction.montant = request.POST['montant']
        transaction.type_paiement = request.POST['type_paiement']
        transaction.save()
        return HttpResponseRedirect('/transactions/')
    achats = Achat.objects.all()
    return render(request, 'transactions/modifier.html', {'transaction': transaction, 'achats': achats})

def supprimer_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return HttpResponseRedirect('/transactions/')
    return render(request, 'transactions/supprimer.html', {'transaction': transaction})

# FACTURES
def liste_factures(request):
    factures = Facture.objects.all()
    return render(request, 'factures/liste.html', {'factures': factures})

def ajout_facture(request):
    if request.method == 'POST':
        achat = Achat.objects.get(id=request.POST['achat'])
        Facture.objects.create(
            achat=achat,
            date=request.POST['date'],
            total=request.POST['total']
        )
        return HttpResponseRedirect('/factures/')
    achats = Achat.objects.all()
    return render(request, 'factures/ajout.html', {'achats': achats})

def index(request):
    return render(request, 'index.html')