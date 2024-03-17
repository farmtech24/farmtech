from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .forms import UserLoginForm, UserRegistrationForm

def iniciar_sesion(request):
    """
    Vista para iniciar sesión de usuario.
    """
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['username']
            clave = form.cleaned_data['password']
            usuario = authenticate(request, username=nombre_usuario, password=clave)
            if usuario is not None:
                login(request, usuario)
                return JsonResponse({'mensaje': 'Inicio de sesión exitoso'})
            else:
                return JsonResponse({'error': 'Nombre de usuario o contraseña incorrectos'}, status=400)
        else:
            return JsonResponse({'error': 'Datos de inicio de sesión no válidos'}, status=400)
    else:
        return JsonResponse({'error': 'Método de solicitud no válido'}, status=405)

def registrar_usuario(request):
    """
    Vista para registrar un nuevo usuario.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password1'])
            usuario.save()
            login(request, usuario)
            return JsonResponse({'mensaje': 'Usuario registrado correctamente'})
        else:
            return JsonResponse({'error': 'Datos de registro no válidos'}, status=400)
    else:
        return JsonResponse({'error': 'Método de solicitud no válido'}, status=405)

def perfil_usuario(request):
    """
    Vista para el perfil de usuario.
    """
    usuario = request.user
    if usuario.is_authenticated:
        return JsonResponse({'username': usuario.username, 'farm_name': usuario.farm.name if usuario.farm else None})
    else:
        return JsonResponse({'error': 'Usuario no autenticado'}, status=401)
