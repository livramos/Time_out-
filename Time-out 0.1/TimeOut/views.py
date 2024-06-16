from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import FormCadastro

# Create your views here.

def home (request):
  return render(request, 'home.html')
  
def cadastro_usuario(request):
  formulario = FormCadastro()
  if request.method == 'POST' and request.POST:
    formulario = FormCadastro(request.POST)
  if formulario.is_valid():
    novo_usuario = formulario.save(commit=False)
    novo_usuario.email = formulario.cleaned_data['email']
    novo_usuario.save()
    return redirect('/login')
  return render(request,'cadastro.html',{'form': formulario})

def login_usuario(request):
 formulario = AuthenticationForm()
 if request.method == 'POST' and request.POST:
  formulario = AuthenticationForm(request, request.POST)
  if formulario.is_valid():
    usuario = formulario.get_user()
    login(request, usuario)
    return redirect('/home_usuario',{'usuario': usuario})
 return render(request, 'login.html', {'form': formulario}) 

@login_required

def logout_usuario(request):
  logout(request)
  return redirect("/home")

def home_usuario(request):
  return render(request,'home_usuario.html',{'usuario':request.user})

def perfil_usuario(request):
  return render(request, 'perfil_usuario.html')
