from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


