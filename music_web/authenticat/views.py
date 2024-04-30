from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User.objects.create_user(username=username, password=password, email=email)  ## at this point the user is already created in the database

        # user.last_name = "something"
        # user.save()                                                            ##  not mandatory only used when updating some properties

        return HttpResponse(username)

    else:
        return render(request, 'login.html')