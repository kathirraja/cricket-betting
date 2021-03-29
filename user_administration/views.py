from django.shortcuts import render,reverse,redirect
from .models import Player, User, Person
from .forms import PlayerForm, TeamForm, MatchForm
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login

# Create your views here.

def create(request, form, action_url):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'POST':
            form = form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_home')
        else:
            form = form()
        return render(request, 'create.html', {'form': form, "action_url":action_url})
    return redirect('user-home')

def create_players(request):
    return create(request, PlayerForm, reverse('create_players'))

def create_team(request):
    return create(request, TeamForm, reverse('create_team'))

def create_match(request):
    return create(request, MatchForm, reverse('create_match'))

def admin_home(request):
    if request.user.is_staff or request.user.is_superuser:
        return render(request, 'admin-home.html')
    elif request.user.is_authenticated:
        return render(request, 'user-home.html')
    else:
        return redirect('my_login')

def my_login(request):
    error=""
    if request.user.is_authenticated:
        return redirect(admin_home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(admin_home)
        else:
            error="Invalid Login"
    return render(request, 'login.html', {"error":error})


def register(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cf_password = request.POST['cf_password']
        if password==cf_password:
            if User.objects.filter(username=username).count()==0:
                user = User.objects.create(username=username)
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                Person.objects.create(user=user)
                login(request, user)
                print (">>>>>>>>>>>", user)
                return redirect (admin_home)
            else:
                error = "Username already exists"
        else:
            error = "Password Mismatch"

    return render(request, 'register.html', {"error":error})

