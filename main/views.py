from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests.api import request
from .models import User 
from .forms import CreateNewUser, UpdateUser
import requests
import json

# Create your views here.

def getusers(response):
    users = User.objects.all()
    context = {'users': users}
    return render(response, "main/list.html", context)

def index(response):
    url = "https://gerador-nomes.herokuapp.com/nome/aleatorio"
    if response.method == "POST":
        form = CreateNewUser(response.POST)
        if form.is_valid():
            nomeRequest = requests.get(url)
            nomeAleatorio = json.loads(nomeRequest.text)
            
            f_nome = nomeAleatorio[0]
            f_sobrenome = nomeAleatorio[1] + ' ' + nomeAleatorio[2]
            f_apelido = form.cleaned_data["apelido"]
            f_email = form.cleaned_data["email"]
            f_idade = form.cleaned_data["idade"]
            f_dataNascimento = form.cleaned_data["dataNascimento"]
            f_obs = form.cleaned_data["obs"]
            newUser = User(nome=f_nome, sobrenome=f_sobrenome, 
                           apelido=f_apelido, email=f_email, 
                           idade=f_idade, dataNascimento=f_dataNascimento, obs=f_obs)
            newUser.save()
            return redirect('/consulta')
            
    else:
        form = CreateNewUser()
    return render(response, "main/register.html", {"form": form})

def beforeUpdateUser(response):
    users = User.objects.all()
    context = {'users': users}
    return render(response, "main/beforeupdate.html", context)

def updateUser(request, pk):
    user = User.objects.get(id=pk)
    form = UpdateUser(instance=user)
    if request.method == 'POST':
        form = UpdateUser(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/consulta')
    
    context = {'form': form, 'user': user}        
    return render(request, 'main/update.html', context)