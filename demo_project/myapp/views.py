from django.shortcuts import render
from django.http import HttpResponse
from .models import django_model


# def index(request):
#     return HttpResponse("Welcome to Django framework")


def students_view(request):
    return render(request, 'home.html')


def datashow_model(request):
    result = django_model.objects.all()
    print(result)
    return render(request, "database_model.html", {"django_model": result})

# Create your views here.
