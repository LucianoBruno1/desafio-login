from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            form = RegisterForm()
    return render(request, 'register.html',{'form':form})





def LoginAction(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)  # Autentica usando o username do usuário
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Email ou senha inválidos')
        except User.DoesNotExist:
            messages.error(request, 'Email ou senha inválidos')

    return render(request, 'login.html')






def LogoutAction(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')
