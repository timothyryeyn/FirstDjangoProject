from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'job_portal/home.html', {'foo': 'bar'})
