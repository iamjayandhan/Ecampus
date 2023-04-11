from django.shortcuts import render
from django.views.generic import ListView
from .models import Student
# Create your views here.
class Home(ListView):
    template_name = "ecam_app/home.html"
    model = Student
    context_object_name = "student"
