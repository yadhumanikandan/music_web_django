from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    return HttpResponse("home page")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # email = request.POST.get("email")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return HttpResponse("authenticated")
        
        else:
            messages.error(request, "bad credentials")
            return HttpResponse(user)

    else:
        return render(request, 'signin.html')
    

def signup(request):
    # if request.user.is_authenticated:
    #     return redirect("signin")
    # username = request.user.username
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        user = User.objects.create_user(username=username, password=password1, email=email)  ## at this point the user is already created in the database

        # user.set_password = password1
        # user.save()                                                            ##  not mandatory only used when updating some properties

        messages.success(request, "you\'r account has been created succesfully")
        return redirect("signin")

    else:
        return render(request, "signup.html")
    

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect("signin")