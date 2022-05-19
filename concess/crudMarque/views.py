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

def stock(request):
    if request.method == "POST":
        form = StockForm(request)
        if form.is_valid():
            stock= form.save()
            return render(request,"crdMarque/stock/affiche.html",{"stock":stock})
        else:
            return render(request,"crdMarque/stock/ajout.html",{"form":form})
    else:
        form = StockForm()
        return render(request, "crdMarque/stock/ajout.html", {"form": form})


def traitement(request):
    mform = MarqForm(request.POST)
    if mform.is_valid():
        voiture=mform.save()
        return render(request,"crdMarque/car1/affiche.html",{"voiture":voiture})
    else:
        return render(request, "crdMarque/car1/ajout.html", {"form": form})

def traitementstock(request):
    stform = StockForm(request.POST)
    if stform.is_valid():
        stock = stform.save()
        return HttpResponseRedirect('/crudMarque/')

    else:
        return render(request, 'Stock/ajout.html', {"form": stform})

def affiche(request, id):
    voiture = models.Marque.objects.get( pk = id )
    return render(request,"crdMarque/car1/affiche.html",{"voiture":voiture})

def affichestock(request, id):
    stock = models.Stock.objects.get( pk = id )
    return render(request,"crdMarque/Stock/affiche.html",{"stock":stock})

def index(request):
    liste=list(models.Marque.objects.all())
    liste2=list(models.Stock.objects.all())
    return render(request,'crdMarque/car1/index.html',{'liste' : liste,'liste2': liste2})




def delete(request, id):
    voiture = models.Marque.objects.get(pk=id)
    voiture.delete()
    return HttpResponseRedirect("/crudMarque/")

def deletestock(request, id):
    stock = models.Stock.objects.get(pk=id)
    stock.delete()
    return HttpResponseRedirect("/crudMarque/")

def update(request,id):
    voiture = models.Marque.objects.get( pk = id )
    form= MarqForm(voiture.dico())
    return render(request, "crdMarque/car1/update.html",{"form":form, "id" : id})

def updatestock(request,id):
    stock = models.Stock.objects.get( pk = id )
    form= StockForm(stock.dicoo())
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

def traitementupdatestock(request, id):
    stform = StockForm(request.POST)
    if stform.is_valid():
        stock = lform.save(commit=False)
        stock.id = id;
        stock.save()
        return HttpResponseRedirect("/crudMarque/")
    else:
        return render(request, "crdMarque/Stock/affiche.html", {"form": stform, "id": id})




