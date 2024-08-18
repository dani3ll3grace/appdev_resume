from django.shortcuts import render
from .models import Project

def home(request):
    print("Home view called")
    return render(request, 'resume_app/home.html')

def work(request):
    print("Work view called")
    return render(request, 'resume_app/work.html')

def about(request):
    print("About view called")
    return render(request, 'resume_app/about.html')

def portfolio(request):
    print("Portfolio view called")
    return render(request, 'resume_app/portfolio.html')

def home(request):
    projects = Project.objects.all()
    return render(request, 'resume_app/home.html', {'projects': projects})
