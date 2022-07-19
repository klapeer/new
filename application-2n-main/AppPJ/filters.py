import django_filters
from django_filters import DateFilter
#from django import django_filters
from .models import Intervention, Panne

class InterventionFiltre(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_intervention", lookup_expr='gte')
    end_date = DateFilter(field_name="date_intervention", lookup_expr='lte')
    class Meta:
        model= Intervention
        fields='__all__'
        exclude=['observation','solution','date_intervention','materiel_en_panne','cout_de_reparation','type_materiel','type_logiciel']
        
class PanneFiltre(django_filters.FilterSet):
    
    class Meta:
        model= Panne
        fields='__all__'
        exclude=['description_panne','materiel','logiciel','date_declaration_panne']
       

