from django.contrib import admin
from .models import  Technicien, Fournisseur, Agence, Typelogiciel, Typemateriel, Materiel, Logiciel, Panne, Intervention

# Register your models here.
   
class AdminTechnicien(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'date_nais', 'email', 'tel', 'adress', 'fonction')
    
class AdminFournisseur(admin.ModelAdmin):
    list_display = ('id', 'raison_social', 'email', 'tel', 'adress', 'years')
     
class AdminAgence(admin.ModelAdmin):
    list_display = ('id', 'nom')
    
class AdminTypemateriel(admin.ModelAdmin):
    list_display = ('id', 'nom')
    
class AdminTypelogiciel(admin.ModelAdmin):
    list_display = ('id', 'nom')
    
class AdminMateriel(admin.ModelAdmin):
    list_display = ('id', 'fournisseur', 'agence', 'type_materiel', 'nom', 'caracteristiques', 'marque', 'autre', 'data_acquisition', 'garantie')

class AdminLogiciel(admin.ModelAdmin):
    list_display = ('id', 'fournisseur', 'agence', 'type_logiciel', 'nom', 'duree_licence', 'data_debut_licence', 'data_fin_licence')
  
class AdminPanne(admin.ModelAdmin):
    list_display = ('id', 'materiel', 'logiciel', 'date_declaration_panne', 'description_panne', 'Etat_panne')
       
#class AdminIntervention(admin.ModelAdmin):
    # = ('id', 'date_intervention', 'panne', 'technicien', 'observation', 'solution', 'Etat_intervention')
    
admin.site.register(Technicien, AdminTechnicien)
admin.site.register(Fournisseur, AdminFournisseur)
admin.site.register(Agence, AdminAgence)
admin.site.register(Typelogiciel, AdminTypelogiciel)
admin.site.register(Typemateriel, AdminTypemateriel)
admin.site.register(Materiel,  AdminMateriel)
admin.site.register(Logiciel, AdminLogiciel)
admin.site.register(Panne, AdminPanne)
admin.site.register(Intervention)



