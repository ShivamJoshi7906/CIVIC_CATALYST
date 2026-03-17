from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, AdminUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'User' # Force role to User
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            print(form.errors)
            messages.error(request, "Registration failed. Please check the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@user_passes_test(lambda u: u.role == 'Admin')
def create_staff_view(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff/Admin account created successfully.')
            return redirect('dashboard')
    else:
        form = AdminUserCreationForm()
    return render(request, 'users/create_staff.html', {'form': form})
