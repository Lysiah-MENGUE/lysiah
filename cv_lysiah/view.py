from django.shortcuts import render
from . email_builder import send_mail_to_client
from . email_builder import send_mail_to_me
from . form import contact_form
def home(request):
    return render(request,'welcome.html');


def moncv(request):
    nom=''
    ok =False
    is_send = False
    if request.method == 'POST':
       form = contact_form(request.POST)
       ok=True
       if form.is_valid():
          name = form.cleaned_data['name']
          email = form.cleaned_data['email']
          message = form.cleaned_data['message']
          entreprise = form.cleaned_data['entreprise']
          is_send = send_mail_to_client(email,name);
          send_mail_to_me(name,entreprise,message,email)  
          nom=name
          
             

    return render(request,"moncv.html",{'form': contact_form,'ok':ok,'is_send':is_send,'nom':nom});    



def certificat(request):

    return render(request,'certificat.html');  


def formation(request):

    return render(request,'formation.html');          


def experience(request):

    return render(request,'experience.html');


def logiciel(request):

    return render(request,'logiciel_outils.html');    