from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

def getAllUsers(request):
    users = UserDetails.objects.all().values('username', 'email')
    return JsonResponse(list(users), safe=False)

def getUserByEmail(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        user_data = {'username': user.username, 'email': user.email}
        return JsonResponse(user_data)
    except UserDetails.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def updateUser(request, email):
    if request.method == 'PUT':
        try:
            user = UserDetails.objects.get(email=email)
            data = json.loads(request.body)
            user.username = data.get('username', user.username)
            user.password = data.get('password', user.password)
            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def deleteUser(request, email):
    if request.method == 'DELETE':
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)