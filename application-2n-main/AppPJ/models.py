from django.db import models
from django.core.validators import RegexValidator

class Agence(models.Model):
    nom = models.CharField(max_length=255, null=True, unique=True)
    
    def __str__(self):
        return self.nom

class Technicien (models.Model):
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE , null = True)
    nom = models.CharField(max_length=250, null=True, unique=True)
    prenom = models.CharField(max_length=250, blank=True)
    date_nais = models.DateField(auto_now_add=False, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True,  blank=True)
    
    tel = models.CharField(max_length=13 , null = True)
   
    adress = models.CharField(max_length=255, null=True)
    fonction = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.nom
    
    
class Fournisseur(models.Model):
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE , null = True)
    raison_social =models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=255, null=True,  blank=True)
    adress = models.CharField(max_length=255, null=True)
    years = models.DateField(auto_now_add=False, null=True)
    tel = models.CharField(max_length=13)
    
    def __str__(self):
        return self.raison_social
    


class Typemateriel(models.Model):
    nom = models.CharField(max_length=255, null=True, unique=True)
    
    def __str__(self):
        return self.nom

class Typelogiciel(models.Model):
    nom = models.CharField(max_length=255, null=True, unique=True)
    
    def __str__(self):
        return self.nom
    
class Materiel(models.Model):
    
    fournisseur = models.ForeignKey(Fournisseur,null=True, on_delete=models.CASCADE)
    agence = models.ForeignKey('Agence',null=True, on_delete=models.CASCADE)
    type_materiel = models.ForeignKey(Typemateriel,null=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, null=True)
    caracteristiques = models.CharField(max_length=255, null=True)
    marque = models.CharField(max_length=255, null=True)
    autre = models.CharField(max_length=255, blank=True, null=True)
    data_acquisition = models.DateField(auto_now_add=False, null=True)
    garantie = models.CharField(max_length=255, null=True,  blank=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['-data_acquisition']
    
class Logiciel(models.Model):
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE , null = True)
    fournisseur = models.ForeignKey(Fournisseur,null=True, on_delete=models.CASCADE)
    agence = models.ForeignKey('Agence',null=True, on_delete=models.CASCADE)
    type_logiciel = models.ForeignKey(Typelogiciel,null=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, null=True)
    duree_licence = models.CharField(max_length=255, null=True)
    data_debut_licence = models.DateField(auto_now_add=False, null=True)
    data_fin_licence = models.DateField(auto_now_add=False, null=True)
    
    def __str__(self):
        return self.nom
    
    
   
    
class Panne(models.Model):
    STATUS=(('Terminer','Terminer'),
            ('En attente','En attente'))
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE , null = True)            
    type_materiel = models.ForeignKey(Typemateriel,null=True, on_delete=models.CASCADE, blank=True)
    type_logiciel = models.ForeignKey(Typelogiciel,null=True, on_delete=models.CASCADE, blank=True)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, blank=True, null=True)
    logiciel = models.ForeignKey(Logiciel, on_delete=models.CASCADE, blank=True, null=True)
    date_declaration_panne = models.DateField(auto_now_add=False, null=True)
    description_panne = models.TextField(help_text='veiller remplir')
    Etat_panne =models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self): 
        return f'{self.materiel},{self.logiciel}'
        
    
    class Meta:
        ordering = ['-date_declaration_panne']
        
        
class Intervention(models.Model):
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE , null = True)
    date_intervention =  models.DateTimeField(auto_now_add=True, null=True)
    panne_concerner = models.ForeignKey('Panne', on_delete=models.CASCADE, null=True)
    technicien = models.ForeignKey('Technicien', on_delete=models.CASCADE,null=True)
    observation = models.TextField()
    solution = models.TextField()
    cout_de_reparation= models.IntegerField(help_text='veiller remplir')
    Etat_intervention = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.date_intervention)
    
    class Meta:
        ordering = ['-date_intervention']
    

    
    
    
    
    
   



