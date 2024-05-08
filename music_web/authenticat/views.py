from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def signin(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already signed in.")
        return redirect("base:home")
    
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect("base:home")
            
            else:
                messages.error(request, "Username or Password incorrect.")
                return redirect("authenticat:signin")

        else:
            return render(request, 'authenticat/signin.html')
    

def signup(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already signed in.")
        return redirect("base:home")
    
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if User.objects.filter(username=username):
                messages.error(request, "Username already exist. Please try another username.")
                return redirect("authenticat:signup")
            
            if User.objects.filter(email=email):
                messages.error(request, "Email already exist. Please try another email.")
                return redirect("authenticat:signup")
            
            if password1 != password2:
                messages.error(request, "Passwords don't match.")
                return redirect("authenticat:signup")

            user = User.objects.create_user(username=username, password=password1, email=email)  ## at this point the user is already created in the database

            messages.success(request, "you\'r account has been created succesfully")
            return redirect("authenticat:signin")

        else:
            return render(request, "authenticat/signup.html")
    

@login_required
def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect("authenticat:signin")