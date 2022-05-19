from django.shortcuts import render
from django.forms import ModelForm
from . import models
from .forms import MarqForm
from django.http import HttpResponseRedirect

# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = MarqForm(request)
        if form.is_valid():
            voiture= form.save()
            return render(request,"crdMarque/car1/affiche.html",{"voiture":voiture})
        else:
            return render(request,"crdMarque/car1/ajout.html",{"form":form})
    else:
        form = MarqForm()
        return render(request, "crdMarque/car1/ajout.html", {"form": form})


def traitement(request):
    mform = MarqForm(request.POST)
    if mform.is_valid():
        voiture=mform.save()
        return render(request,"crdMarque/car1/affiche.html",{"voiture":voiture})
    else:
        return render(request, "crdMarque/car1/ajout.html", {"form": form})

def affiche(request, id):
    voiture = models.Marque.objects.get( pk = id )
    return render(request,"crdMarque/car1/affiche.html",{"voiture":voiture})

def index(request):
    liste=list(models.Marque.objects.all())
    return render(request,'crdMarque/car1/index.html',{'liste' : liste})




def delete(request, id):
    voiture = models.Marque.objects.get(pk=id)
    voiture.delete()
    return HttpResponseRedirect("/crudMarque/")

def update(request,id):
    voiture = models.Marque.objects.get( pk = id )
    form= MarqForm(voiture.dico())
    return render(request, "crdMarque/car1/update.html",{"form":form, "id" : id})

def traitementupdate(request, id):
    lform = MarqForm(request.POST)
    if lform.is_valid():
        voiture = lform.save(commit=False)
        voiture.id = id;
        voiture.save()
        return HttpResponseRedirect("/crudMarque/")
    else:
        return render(request, "crdMarque/car1/affiche.html", {"form": lform, "id": id})



