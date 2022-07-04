import random

from django.shortcuts import render


def home(request):
    lst = list(range(6, 15))
    return render(request, "generator/home.html", {'lst': lst})


def password(request):
    psw = ''
    char = [chr(i) for i in range(97, 123)]
    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])
    if request.GET.get('numbers'):
        char.extend([str(i) for i in range(10)])
    if request.GET.get('special'):
        char.extend(list(r"-=+!@#$%^&*()\|/"))
    length = int(request.GET.get('length'))
    for i in range(length):
        psw += random.choice(char)
    return render(request, "generator/password.html", {'password': psw})


def rules(request):
    return render(request, "generator/rules.html")
