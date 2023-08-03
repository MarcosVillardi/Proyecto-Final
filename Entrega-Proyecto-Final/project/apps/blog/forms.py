from django import forms
from . import models

class ReservaForm(forms.ModelForm):
    class Meta:
        model = models.Reserva
        fields = '__all__'

class GarajeForm(forms.ModelForm):
    class Meta:
        model = models.Garaje
        fields = '__all__'