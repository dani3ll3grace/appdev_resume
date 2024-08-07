from django.shortcuts import render
from .models import Project, Skill

from django.shortcuts import render

def home(request):
    return render(request, 'resume_app/home.html')

def work(request):
    return render(request, 'resume_app/work.html')

def about(request):
    return render(request, 'resume_app/about.html')

def portfolio(request):
    return render(request, 'resume_app/portfolio.html')
