from django.shortcuts import render, get_object_or_404
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

def home(request):
    projects = Project.objects.all()
    return render(request, 'resume_app/home.html', {'projects': projects})

def work(request):
    projects = Project.objects.all()
    return render(request, 'resume_app/work.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'resume_app/project_detail.html', {'project': project})