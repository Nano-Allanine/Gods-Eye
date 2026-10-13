from .models import Student
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    students = Student.objects.all()
    context = {
        'std ': students
    }
    return render(request, "home.html", context)
