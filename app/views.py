from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView
from app.models import *

class home(TemplateView):
    model='School'
    template_name='app/home.html'

class student_list(ListView):
    model=School
    template_name='app/student_list.html'
    context_object_name='schools'