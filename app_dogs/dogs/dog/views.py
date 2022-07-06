from django.shortcuts import render, get_object_or_404

from dog.models import Dog


def index(request):
    dogs = Dog.objects.all()
    return render(request, 'dog/index.html', {'dogs': dogs})


def info(request, dog_id):
    dogs = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'dog/info.html', {'dogs': dogs})
