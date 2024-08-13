from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import CustomUser, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate form data
        if not (name and email and password):
            return render(request, 'core/signup.html', {'error': 'All fields are required'})

        # Check if user with given email already exists
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'core/signup.html', {'error': 'Email is already taken'})

        # Create user
        user = CustomUser.objects.create_user(
            name=name,
            email=email,
            password=password
        )

        # Redirect to login page or any other page
        return redirect('login')  # Change 'login' to your actual login page URL

    return render(request, 'core/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid email or password. Please try again.'
            return render(request, 'core/login.html', {'error': error})

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    try:
        # Attempt to retrieve the UserProfile associated with the logged-in user
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If UserProfile does not exist, handle the error gracefully
        user_profile = None  # Set user_profile to None or handle the absence of the profile as needed

    return render(request, 'core/dashboard.html', {'user_profile': user_profile})