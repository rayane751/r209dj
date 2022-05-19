from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class MarqForm(ModelForm):
    class Meta:
        model = models.Marque
        fields = ('nom', 'modele', 'year','pays' ,'chevaux')
        labels = {
            'nom' : _('Marque'),
            'modele' : _('Modèle') ,
            'year' : _('Date de première mise en circulation'),
            'pays' : _('Pays'),
            'chevaux' : _('Chevaux')
        }
        localized_fields = ('year',)
