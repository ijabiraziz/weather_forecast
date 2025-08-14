from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

class SignupView(View):
    def get(self, request):
        return render(request, 'accounts/signup.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect('signup')
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created. Please log in.")
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('predict_rain')
        messages.error(request, "Invalid credentials")
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
