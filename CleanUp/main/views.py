from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from .models import *

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid username and password'})
        
    return render(request, 'main/login.html')
    
def signup(request):

    if request.method == 'POST':
        
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "main/signup.html", {
                "error": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "main/signup.html", {
                "error": "Email address already taken."
            })
        
        login(request, user)
        return redirect('home')
    
    return render(request, 'main/signup.html')

def home(request):
    return render(request, 'main/home.html')