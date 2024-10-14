from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('Loginify:signup')
        
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('Loginify:login')
    
    return render(request, 'Loginify/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = UserDetails.objects.get(email=email, password=password)
            messages.success(request, 'Login successful')
            return render(request, 'Loginify/success.html')
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'Loginify/login.html')