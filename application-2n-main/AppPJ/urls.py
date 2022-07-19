from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.login_page, name="login_page"),
    path('list_ag', views.list_agence, name="list_agence"),
    path('accueil', views.accueil, name="accueil"),
    path('Quitter', views.logout_user, name="logout_user"),
    path('inscription', views.inscripton_page, name="inscription_page"),
    path('home/<str:pk>', views.home, name="home"),  
    path('tableau/<str:pk>', views.home, name="tableau"),  
    path('statiq/', views.statistique, name="statistique"), 
    path('addAgence/', views.addAgence, name="addAgence"), 
    # path('savePanne/', views.savePanne, name="savePanne"), 
    
    
    
    path('pdf_interv', views.pdf_interv, name='pdf_interv'),
    
    path('add_panne', views.add_panne, name="add_panne"),
    path('modal', views.modal, name="modal"),
    path('add_panneL', views.add_panneL, name="add_panneL"),
    path('list_panne', views.list_panne, name="panne"),
    path('modifier_panne/<str:pk>',views.modifier_panne, name='modifier_panne'),
    path('modifier_panneL/<str:pk>',views.modifier_panneL, name='modifier_panneL'),
    # path('supprimer_panne/<str:pk>',views.supprimer_panne, name='supprimer_panne'),
       
    path('add_intervention/<str:materiel_en_panne>', views.add_intervention, name="add_interv"),
    path('list_intervention', views.list_intervention, name="intervention"),
    path('detail_intervention/<str:pk>',views.detail_intervention, name='detail_intervention'),
    path('detail_panne',views.detail_panne, name='detail_panne'),
    path('modifier_intervention/<str:pk>',views.modifier_intervention, name='modifier_intervention'),
    path('population-chart/', views.population_chart, name='population-chart'), 
    path('ajax/load-mat/', views.load_materiel, name='ajax_load_mat')
]
