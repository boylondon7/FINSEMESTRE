from django.db import models

# Create your models here.

#Model pour la class Categorie
class Categorie(models.Model):
    nom = models.CharField(max_length=255)



#Model pour la class Produit
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.FloatField()
    quantite = models.IntegerField()
    description = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')

    

#Model pour la class Client
class Client(models.Model):
    nom = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)


#Model pour la class Achat
class Achat(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='achats')
    date = models.DateField()

   

#Model pour la class PanierClient
class PanierClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='panier_clients')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='panier_clients')
    quantite = models.IntegerField()


#Model pour la class Transaction

class Transaction(models.Model):
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, related_name='transactions')
    montant = models.FloatField()
    type_paiement = models.CharField(max_length=100)

    

#Model pour la class Facture
class Facture(models.Model):
    achat = models.OneToOneField(Achat, on_delete=models.CASCADE, related_name='facture')
    date = models.DateField()
    total = models.FloatField()


    