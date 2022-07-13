
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from .forms import TodoForm
from .models import Todo


def home(request):
    return render(request, 'todo/home.html')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'Такое имя существует, задайте другое имя'})
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),
                                                            'error': 'Пароли не совпадают'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def currenttodos(request):
    user = request.user
    tasks = Todo.objects.filter(user=user).order_by('-created')
    return render(request, 'todo/currenttodos.html', {"tasks": tasks})

    # return render(request, 'todo/currenttodos.html')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('currenttodos')


def createtodo(request):
    if request.method == "GET":
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        user = request.user
        title = request.POST["title"]
        memo = request.POST["memo"]
        if request.POST.get("important"):
            important = True
        else:
            important = False
        task = Todo(title=title, memo=memo, user=user, important=important)
        task.save()
        tasks = Todo.objects.filter(user=user).order_by('-created')
        return render(request, 'todo/currenttodos.html', {"tasks": tasks})

