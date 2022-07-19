# #from django.core.paginator import Paginator, EmptyPage
# from cgitb import html
# from multiprocessing import context
# from re import template
# from turtle import ht
# from urllib import response
import imp
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
from AppPJ.forms import PanneForm, InterventionForm, AgenceForm
from AppPJ.models import Logiciel, Materiel, Panne, Intervention, Agence, Typelogiciel,Typemateriel
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from AppPJ.filters import InterventionFiltre, PanneFiltre
from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa
from django.db.models import F
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import JsonResponse
from django.urls import reverse_lazy
import json


#ici on enregistre une nouvelle agence
def addAgence(request):
    form = AgenceForm()
    if request.method == 'POST':
        form = AgenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    context = {
        'form':form,
        }
    return render(request, 'pages/agenceadd.html',context)

#ici on enregistre les pannes

# def savePanne(request):
#     form = PanneForm()
#     if request.method == 'POST':
#         form = PanneForm(request.POST)
#     return render(request, 'pages/add_panne.html',context)




# products = customer.order_set.all()
def home(request,pk):
    list_ag = Agence.objects.get(id=pk)
    var_interv_count = list_ag.intervention_set.all().count()
    var_panne_count = list_ag.panne_set.all().count()
    var_mat_count = list_ag.materiel_set.all().count() 
    var_cout_interv = list_ag.intervention_set.all().aggregate(thedata=Sum('cout_de_reparation'))
    se_no = list_ag.intervention_set.filter(Etat_intervention='True').count()
    se_no = int(se_no)
    print('Number of Software Engineering Students Are',se_no)
    sec_no = list_ag.intervention_set.filter(Etat_intervention='False').count()
    sec_no = int(sec_no)
    print('Number of Computer Security Students Are',sec_no)
    
    
    return render(request, 'pages/index.html', {'list_ag':list_ag,'var_interv_count':var_interv_count,'var_panne_count':var_panne_count,'var_mat_count':var_mat_count,'var_cout_interv':var_cout_interv,'se_no':se_no,'sec_no':sec_no})
    



# def list_agence(request):
#     list_ag=Agence.objects.all()
#     #var_agence = Agence.objects.get(id=pk)
#     return render(request, 'pages/agence_list.html', {'list_ag':list_ag})

def logout_user(request):
    logout(request)
    return redirect('login_page')
    

#--------fonction concernant la page accueil-------------#
def accueil(request):
    list_ag=Agence.objects.all()
    
    return render(request, 'pages/accueil.html', {'list_ag':list_ag})

def list_agence(request):
    list_ag=Agence.objects.all()
    #var_agence = Agence.objects.get(id=pk)
    return render(request, 'pages/agence_list.html', {'list_ag':list_ag})

#-------------------fonction pour ce login--------------------------------------------------------------------------- 

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accueil')
        else:
            messages.info(request,"Uilisateur ou Password non valide")
    return render(request,'pages/login.html')

def inscripton_page(request):
    form=CreerUtilisateur()
    if request.method =='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'compte creer avec success pour '+user)
            
    context={'form':form}
    return render(request,'pages/inscription.html',context)

# -----------------------les fonction pour panne------------------------------------------------------

def list_panne(request):
    var_panne = Panne.objects.all()    
    myFilter= PanneFiltre(request.GET,queryset=var_panne)
    var_panne=myFilter.qs
    vpaginator= Paginator(var_panne, 2)
    vpage_nuber= request.GET.get('page')
    vpage_object= vpaginator.get_page(vpage_nuber)
    
    vpage_nuber = var_panne.count()
    vsms= f'{vpage_nuber} posts:'
    
    if vpage_nuber == 1:
        vsms= f'{vpage_nuber} post:'
    return render(request, 'pages/panne_list.html', {'var_panne': var_panne, 'myFilter':myFilter, 'vpage_object':vpage_object})


def add_panne(request):
    form = PanneForm()
    if request.method=='POST':
        form = PanneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panne')
    else:
        pass
    
    context = {'form':form,}  
    return render(request,'pages/add_panne.html', context)

# def add_panne(request):
#     panne = Panne.objects.all()
#     success_url = reverse_lazy('panne')
#     if request.method=='POST':
#         form = PanneForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('panne')
        
#     context = {'form':form,'success_url':success_url}
#     return render(request, 'pages/add_panne.html', context)

def load_materiel(request):
    typemat_id = request.GET.get('type_materiel')
    var_mat = Materiel.objects.filter(typemat_id=typemat_id).order_by('nom')
    return render(request, 'pages/mat_options.html', {'var_mat': var_mat})

def modal(request):

    return render(request, 'pages/modal.html')


def add_panneL(request):
    form = PanneForm()
    if request.method=='POST':
        form = PanneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panne')
    context = {'form':form}
    return render(request, 'pages/add_panneL.html', context)

def modifier_panne(request, pk):
    panne=Panne.objects.get(id=pk)
    form = PanneForm(instance=panne)
    
    if request.method=='POST':
        form = PanneForm(request.POST,instance=panne)
        if form.is_valid():
            form.save()
            return redirect('panne')
        
    context = {'form':form}
    return render(request, 'pages/add_panne.html', context)

def modifier_panneL(request, pk):
    intervention=Panne.objects.get(id=pk)
    form = PanneForm(instance=intervention)
    
    if request.method=='POST':
        form = PanneForm(request.POST,instance=intervention)
        if form.is_valid():
            form.save()
            messages.success(request, "Edit Info Successfully!")
            return redirect('panne')
        
    context = {'form':form}
    return render(request, 'pages/add_panneL.html', context)

# def supprimer_panne(request, pk):
#     panne=Panne.objects.get(id=pk)
#     if request.method=='POST':
#         panne.delete()
#         return redirect('/')
#     context={'item':panne}
   
#     return render(request, 'commande/supprimer_commande.html', context)

# --------------------les fonctions interv----------------------------------------------------
def add_intervention(request,materiel_en_panne):
    intervall=Intervention.objects.all()
    intervention=Intervention.objects.filter(pk=materiel_en_panne).first()
    form = InterventionForm(instance=intervention)
    if request.method=='POST':
        form = InterventionForm(request.POST,instance=intervention)
        if form.is_valid():
            form.save()
            return redirect('intervention')
        
    context = {'form':form, 'intervall':intervall}
    return render(request, 'pages/add_interv.html', context)


def modifier_intervention(request, pk):
    intervention=Intervention.objects.get(id=pk)
    form = InterventionForm(instance=intervention)
    
    if request.method == 'POST':
        form = InterventionForm(request.POST,instance=intervention)
        if form.is_valid():
            form.save()
            messages.success(request, "Edit Info Successfully!")
            return redirect('intervention')
        
    context = {'form':form}
    return render(request, 'pages/add_interv.html', context)

# def detail_intervention(request):
   
#     return render(request, 'pages/detail_interv.html')

def detail_panne(request):
   
    return render(request, 'pages/detail_panne.html')

def detail_intervention(request, pk):
    var_interv = Intervention.objects.get(id=pk)     
    context = {
        'var_interv':var_interv,
    }  
    return render(request, 'pages/detail_interv.html', context)


def pdf_interv(request):
    var_interv = Intervention.objects.all()
    myFilter= InterventionFiltre(request.GET,queryset=var_interv)
    var_filter=myFilter.qs
   
    fil_interv = var_filter.filter(date_intervention__year=F('date_intervention__year'))
    template_path = 'pages/pdf_interv.html'
    context = {'var_interv':var_interv, 'fil_interv':fil_interv}
    response= HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="intervention.pdf"'
    template= get_template(template_path)
    html = template.render(context)
    
     # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def list_intervention(request):  
    var_interv = Intervention.objects.all()
    
    myFilter= InterventionFiltre(request.GET,queryset=var_interv)
    var_interv=myFilter.qs
    #context={'client':client, 'commande':commande,'commande_total':commande_total, 'myFilter':myFilter}
    #return render(request, 'client/list_client.html',context)
    return render(request, 'pages/interv_list.html', {'var_interv': var_interv, 'myFilter':myFilter})



def population_chart(request):
    labels = []
    data = []

    queryset = Intervention.objects.values('panne_concerner__date_declaration_panne').annotate(country_population=Sum('cout_de_reparation')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['panne_concerner__date_declaration_panne'])
        data.append(entry['country_population'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
    
def statistique(request):
    cs_no = Panne.objects.filter(Etat_panne='Encours').count()
    cs_no = int(cs_no)
    print('Number of Computer Science Students Are',cs_no)

    ce_no = Panne.objects.filter(Etat_panne='En attente').count()
    ce_no = int(ce_no)
    print('Number of Computer Engineering Students Are',ce_no)



    se_no = Intervention.objects.filter(Etat_intervention='True').count()
    se_no = int(se_no)
    print('Number of Software Engineering Students Are',se_no)

    sec_no = Intervention.objects.filter(Etat_intervention='False').count()
    sec_no = int(sec_no)
    print('Number of Computer Security Students Are',sec_no)

    gender_list = ['Encours', 'En attente']
    gender_number = [cs_no, ce_no]
    
    gender_list_interv = ['Intervention Termine', 'Intervention En manque']
    gender_number_interv = [se_no, sec_no]
    

    context = {'gender_list':gender_list, 'gender_number':gender_number,'gender_list_interv':gender_list_interv,'gender_number_interv':gender_number_interv}
    return render(request, 'pages/dashboard.html', context)

