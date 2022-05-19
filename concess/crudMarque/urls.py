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

    path('stock/', views.stock),
    path('traitementstock/', views.traitementstock),
    path("deletes/<int:id>", views.deletestock),
    path('affiches/<int:id>/', views.affichestock, name="affs"),
    path('updates/<int:id>/', views.updatestock),
    path("traitementupdates/<int:id>", views.traitementupdatestock),



]
