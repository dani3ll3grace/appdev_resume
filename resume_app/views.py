from django.shortcuts import render

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
