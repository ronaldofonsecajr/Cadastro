from django.shortcuts import render
from .models import Usuario

def home(request):
    return render (request,'usuarios/home.html')

def usuarios(resquest):
    novo_usuario = Usuario()
    novo_usuario.nome = resquest.POST.get('nome')
    novo_usuario.idade = resquest.POST.get('idade')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(resquest,'usuarios/usuarios.html',usuarios)