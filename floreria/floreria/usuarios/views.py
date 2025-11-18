from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # En la validación de campos vacíos
        if not usuario or not password:
            messages.error(request, 'El nombre de usuario y la contraseña son obligatorios.')
            return redirect('usuarios:registro')

        # 1. VERIFICACIÓN DE EXISTENCIA
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuario ya existe.')
            return render(request, 'usuarios/registro.html', {'email': email}) 
        
        # 2. CREACIÓN EXITOSA
        else:
            User.objects.create_user(username=usuario, email=email, password=password)
            messages.success(request, 'Cuenta creada. Inicia sesión.')
            return redirect('usuarios:login') # Redirige al login

    # Si es una solicitud GET
    return render(request, 'usuarios/registro.html')