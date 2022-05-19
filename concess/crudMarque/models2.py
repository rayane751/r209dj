from django.db import models


class Stock (models.Model):
    couleur = models.CharField(max_length=100)
    pack = models.CharField(max_length=50)
    prix = models.CharField(max_length= False)

    quantite = models.IntegerField(blank = True)

    def __str__(self):

        chaine = f" {self.couleur} avec le pack {self.pack} ,il y en a {self.quantite} , à partir de {self.prix}"

        return chaine
    def dicoo(self):
        return  {"couleur": self.couleur,"pack":self.pack,"quantité":self.quantite,"prix":self.prix}