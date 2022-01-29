from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from job_portal.models import Job

# Create your views here.
def home(request):
    if not request.user.is_authenticated: return redirect(settings.LOGIN_URL)
    
    context = {
        'jobs': Job.objects.all()
    }
    return render(request, 'job_portal/pages/home.html', context)
