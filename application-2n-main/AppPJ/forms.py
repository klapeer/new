from django import forms
from django.forms import ModelForm
from .models import Agence, Intervention, Logiciel, Materiel, Panne, Technicien,Typemateriel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings



        
class LogicielForm(forms.ModelForm):
    class Meta:
        model = Logiciel
        fields = '__all__'

        
class TechnicienForm(forms.ModelForm):
    class Meta:
        model = Technicien
        fields = '__all__'

class AgenceForm(ModelForm):
    class Meta:
        model = Agence
        fields = '__all__'
    
class PanneForm(forms.ModelForm):
    class Meta:
        model = Panne
        fields = '__all__'
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['materiel'].queryset = Materiel.objects.none()
        
    #     if 'typemateriel' in self.data:
    #         try:
    #             typemateriel_id = int(self.data.get('type_materiel'))
    #             self.fields['materiel'].queryset = Materiel.objects.filter(typemateriel_id=typemateriel_id).order_by('nom')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['materiel'].queryset = self.instance.typemateriel.materiel_set.order_by('nom')
              
class InterventionForm(forms.ModelForm):
    start_date=forms.DateTimeField(required=False)
    end_date=forms.DateTimeField(required=False)
    class Meta:
        model = Intervention
        fields = '__all__'
        
class CreerUtilisateur(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
