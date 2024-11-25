from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if user.user_type=='vendedor':
                    # return HttpResponse('Vendedor')
                    return redirect('seller_dashboard')
                else:
                    return HttpResponse('otro')
                    # return redirect('home')
            else:
                form.add_error(None, 'Email o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})