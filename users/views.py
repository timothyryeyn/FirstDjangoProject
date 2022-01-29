from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
from job_portal.models import Provider, Seeker
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            type = form.cleaned_data.get('type')
            
            if type == 1:
                seeker = Seeker(user=user)
                seeker.save()
            else:
                provider = Provider(user=user)
                provider.save()

            messages.success(request, 'Account created!')
            return redirect('login')
    else: 
        form = UserRegisterForm()

    return render(request, 'users/pages/register.html', { 'form': form })

def profile(request):
    if not request.user.is_authenticated: return redirect(settings.LOGIN_URL)

    return render(request, 'users/pages/profile.html')
