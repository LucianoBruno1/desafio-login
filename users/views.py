import re

from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        #Validação do nome (apenas letras)
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", name):
            messages.error(request, "O nome deve conter apenas letras e espaços.")
            return redirect("register")

        #Validação do e-mail
        if "@" not in email or "." not in email:
            messages.error(request, "E-mail inválido.")
            return redirect("register")

        #Validação da senha
        if len(password) < 8 or not re.search(r"\d", password) or not re.search(r"[A-Z]", password) or not re.search(
                r"[!@#$%^&*(),.?\":{}|<>]", password):
            messages.error(request,
                           "A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiúscula, um número e um caractere especial.")
            return redirect("register")

        #Verificação da confirmação da senha
        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("register")

        #Verificação se o e-mail já está cadastrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado.")
            return redirect("register")

        #Criando o usuário
        user = User.objects.create_user(username=name, email=email, password=password, first_name=name)
        messages.success(request, "Conta criada com sucesso! Faça login.")
        return redirect("login")

    return render(request, "register.html")


def LoginAction(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        #Verifica se o email existe no banco de dados
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "E-mail inexistente")
            return redirect("login")

        #Verifica se a senha foi informada
        if not password:
            messages.error(request, "Senha inexistente")
            return redirect("login")

        #Autentica o usuário
        user = authenticate(request, username=user.username, password=password)
        if user is None:
            messages.error(request, "Senha inválida")
            return redirect("login")

        #Login bem-sucedido
        login(request, user)
        return redirect("home")  # Substitua 'home' pela URL correta da sua página inicial

    return render(request, "login.html")






def LogoutAction(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
