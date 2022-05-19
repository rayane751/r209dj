from django.db import models


# Create your models here.

class Marque (models.Model):
    nom = models.CharField(max_length=100)
    modele = models.CharField(max_length=50)
    pays = models.CharField(max_length=30)
    year = models.DateField(blank=False)
    chevaux = models.IntegerField(blank = True)

    def __str__(self):

        chaine = f"La {self.nom} {self.modele} ,voiture venant du pays : {self.pays} , mise en circulation le {self.year} développant au minimum {self.chevaux} chevaux"

        return chaine
    def dico(self):
        return  {"Marque": self.nom,"modele":self.modele,"pays":self.pays,"année":self.year,"chevaux":self.chevaux}


