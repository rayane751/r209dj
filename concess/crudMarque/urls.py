from django.urls import path
from . import views
urlpatterns = [

    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path("",views.index, name="index"),
    path("delete/<int:id>", views.delete),
    path('affiche/<int:id>/',views.affiche, name="aff"),
    path('update/<int:id>/',views.update),
    path("traitementupdate/<int:id>",views.traitementupdate),





]
