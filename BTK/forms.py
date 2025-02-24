from django import forms
from .models import Categorie, Produit, Client, Achat, PanierClient, Transaction, Facture

class CategorieForm(forms.Form):
    nom = forms.CharField(label="Nom de la catégorie", max_length=255)

class ProduitForm(forms.Form):
    nom = forms.CharField(label="Nom du produit", max_length=255)
    prix = forms.FloatField(label="Prix")
    quantite = forms.IntegerField(label="Quantité")
    description = forms.CharField(label="Description", max_length=255, widget=forms.Textarea)
    categorie = forms.ModelChoiceField(label="Catégorie", queryset=Categorie.objects.all())

class ClientForm(forms.Form):
    nom = forms.CharField(label="Nom du client", max_length=255)
    contact = forms.CharField(label="Contact", max_length=255)

class AchatForm(forms.Form):
    client = forms.ModelChoiceField(label="Client", queryset=Client.objects.all())
    date = forms.DateField(label="Date d'achat", widget=forms.DateInput(attrs={'type': 'date'}))

class PanierClientForm(forms.Form):
    client = forms.ModelChoiceField(label="Client", queryset=Client.objects.all())
    produit = forms.ModelChoiceField(label="Produit", queryset=Produit.objects.all())
    quantite = forms.IntegerField(label="Quantité")

class TransactionForm(forms.Form):
    achat = forms.ModelChoiceField(label="Achat", queryset=Achat.objects.all())
    montant = forms.FloatField(label="Montant")
    type_paiement = forms.ChoiceField(label="Type de paiement",choices=[('Espèces', 'Espèces'),('Carte bancaire', 'Carte bancaire'), ('Chèque', 'Chèque'),('Virement', 'Virement'),] )

class FactureForm(forms.Form):
    achat = forms.ModelChoiceField(label="Achat", queryset=Achat.objects.all())
    date = forms.DateField(label="Date de facture", widget=forms.DateInput(attrs={'type': 'date'}))
    total = forms.FloatField(label="Total")
