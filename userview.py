from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser, CreditRequest

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def request_credits(request):
    if request.method == 'POST':
        requested_credits = int(request.POST['credits'])
        CreditRequest.objects.create(user=request.user, requested_credits=requested_credits)
    return redirect('dashboard')

def approve_credits(request, request_id):
    credit_request = CreditRequest.objects.get(id=request_id)
    credit_request.user.credits += credit_request.requested_credits
    credit_request.user.save()
    credit_request.approved = True
    credit_request.save()
    return redirect('admin_dashboard')
