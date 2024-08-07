from django.contrib import admin
from django.urls import path, include
from resume_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume_app.urls')),
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
