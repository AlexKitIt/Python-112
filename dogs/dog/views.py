from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from dog.forms import DogForm
from dog.models import Dog


def index(request):
    return render(request, 'dog/index.html')


def signup(request):
    if request.method == "GET":
        return render(request, 'dog/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('info')

            except IntegrityError:
                return render(request, 'todo/signup.html', {'form': UserCreationForm(),
                                                            'error': 'Такое имя существует, задайте другое имя'})
        else:
            return render(request, 'todo/signup.html', {'form': UserCreationForm(),
                                                        'error': 'Пароли не совпадают'})


def login_user(request):
    if request.method == "GET":
        return render(request, 'dog/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'dog/login.html', {'form': AuthenticationForm(),
                                                      'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('info')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


@login_required
def info(request):
    pets = Dog.objects.all()
    return render(request, 'dog/info.html', {"pets": pets})


@login_required
def add_pet(request):
    if request.method == "GET":
        return render(request, 'dog/add_pet.html', {'form': DogForm()})
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.POST["image"]
        pet = Dog(title=title, description=description, image=image)
        pet.save()
        pets = Dog.objects.all()
        return render(request, 'dog/info.html', {"pets": pets})
