
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def inicio(request):
    return render(request, 'web/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('panel')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'web/login.html')


def panel(request):
    if not request.user.is_authenticated:
        return redirect('login')

    contexto = {
        'usuarios': 120,
        'ventas': 85,
        'vehiculos': 240,
        'recomendaciones': 12,
    }

    return render(request, 'web/panel.html', contexto)
