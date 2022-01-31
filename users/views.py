from pprint import pprint
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, ProviderForm, SeekerForm
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


def viewProfile(request):
    if not request.user.is_authenticated: return redirect(settings.LOGIN_URL)

    return render(request, 'users/pages/profile.html')


def editProfile(request):
    if not request.user.is_authenticated: return redirect(settings.LOGIN_URL)

    seekerForm = SeekerForm()
    providerForm = ProviderForm()

    if getattr(request.user, 'provider', None) is not None:
        if request.method == 'POST':
            providerForm = ProviderForm(request.POST)
            if providerForm.is_valid():
                details = providerForm.cleaned_data
                Provider.objects.filter(user_id=request.user.id).update(**details)
                return redirect('profile')

        provider = request.user.provider
        providerForm = ProviderForm(
            initial={
                'name': provider.name,       
                'city': provider.city,       
                'about': provider.about,       
                'country': provider.country,       
            }
        )
    else:
        if request.method == 'POST':
            seekerForm = SeekerForm(request.POST, request.FILES)
            if seekerForm.is_valid():
                details = seekerForm.cleaned_data

                Seeker.objects.filter(user_id=request.user.id).first().seekerskill_set.all().delete()
                for seekerskill in details['seekerskill']:
                    Seeker.objects.filter(user_id=request.user.id).first().seekerskill_set.create(skill=seekerskill)
                details.pop('seekerskill')

                Seeker.objects.filter(user_id=request.user.id).update(**details)
                return redirect('profile')

        seeker = request.user.seeker
        seekerForm = SeekerForm(
            initial={
                'full_name': seeker.full_name,       
                'about_me': seeker.about_me,       
                'experience': seeker.experience,       
                'resume': seeker.resume,
                'seekerskill': [
                    skill for skill in Seeker.objects.filter(user_id=request.user.id).first().seekerskill_set.all().values_list("skill_id", flat=True)
                ]
            }
        )

    return render(
        request, 
        'users/pages/edit-profile.html', 
        { 
            'providerForm': providerForm,
            'seekerForm': seekerForm
        }
    )

