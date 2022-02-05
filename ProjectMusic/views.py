from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ProjectMusic.forms import UserRegisterForm

#Logueo de usuario!

def login_request(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, request.POST)
       
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
               login(request, user)
               return redirect ('inicio')
            else:
                return render(request, 'login.html',
                    {'form': form,
                     'error': 'No es válido el usuario y contraseña'})
        else:
            return redirect('inicio')
    else:
        form= AuthenticationForm()
        return render(request, 'AppMusic/login.html', {'form' : form})
    

#Registro de usuario!

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
           username = form.cleaned_data['username']
           form.save()
           return redirect('inicio')
         
            
    else:
        form = UserRegisterForm()
        
    return render(request, 'AppMusic/register.html', {'form': form})
    