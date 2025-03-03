from django.shortcuts import render
from .forms import LoginForm, CadastroForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is None: 
            return render(request, 'login.html', {'form': form, 'error': 'Credenciais inválidas.'})

        login(request, user)
        return redirect('perfil')  # Redirecionar para a página de perfil após o login
    return render(request, 'login.html', {'form': form})  # Renderizar a página de login



def cadastro(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print(f"User created: {username}, Email: {email}")  # Log para depuração
        return redirect('login')  # Redirecionar para a página de login após o cadastro

    print("Form is not valid:", form.errors)  # Log para depuração
    return render(request, 'cadastro.html', {'form': form})  # Renderizar a página de cadastro

def user(request):
    return render(request, 'user.html')

@login_required
def perfil(request):

    return render(request, 'perfil.html', {'user': request.user})


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Atualizar as informações do usuário
        request.user.first_name = request.POST.get('nome')
        request.user.email = request.POST.get('email')
        request.user.profile.biografia = request.POST.get('biografia')  # Supondo que haja um campo biografia no modelo de perfil
        request.user.save()
        return redirect('perfil')  # Redirecionar para a página de perfil após a atualização

    return render(request, 'editar_perfil.html')  # Renderizar a página de edição de perfil
