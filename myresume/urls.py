from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from resume_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume_app.urls')),
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
