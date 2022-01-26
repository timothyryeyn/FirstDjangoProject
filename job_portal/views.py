from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from job_portal.models import Job

# Create your views here.
def home(request):
    context = {
        'jobs': Job.objects.all()
    }
    return render(request, 'job_portal/pages/home.html', context)
