from django.db import models

# Create your models here.


class Categorie(models.Model):
    nom = models.CharField(max_length=255)

   

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.FloatField()
    quantite = models.IntegerField()
    description = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')

    

class Client(models.Model):
    nom = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)


class Achat(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='achats')
    date = models.DateField()

   

class PanierClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='panier_clients')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='panier_clients')
    quantite = models.IntegerField()

    

class Transaction(models.Model):
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, related_name='transactions')
    montant = models.FloatField()
    type_paiement = models.CharField(max_length=100)

    

class Facture(models.Model):
    achat = models.OneToOneField(Achat, on_delete=models.CASCADE, related_name='facture')
    date = models.DateField()
    total = models.FloatField()


    