from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='job_portal-home'),
]
