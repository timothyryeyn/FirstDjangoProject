from pprint import pprint
from django.contrib.auth.decorators import login_required
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


@login_required
def viewProfile(request):

    return render(request, 'users/pages/profile.html')


@login_required
def editProfile(request):

    seekerForm = SeekerForm()
    providerForm = ProviderForm()
    seeker = None
    seekerResumeUrl = None
    provider = None

    if getattr(request.user, 'provider', None) is not None:
        provider = request.user.provider

        if request.method == 'POST':
            providerForm = ProviderForm(instance=provider, data=request.POST)
            if providerForm.is_valid():
                providerForm.save()
                return redirect('profile')
        
        providerForm = ProviderForm(
            initial={
                'name': provider.name,       
                'city': provider.city,       
                'about': provider.about,       
                'country': provider.country,       
            }
        )
    else:
        seeker = request.user.seeker

        if seeker.resume:
            seekerResumeUrl = seeker.resume.url

        if request.method == 'POST':
            seekerForm = SeekerForm(instance=seeker, data=request.POST, files=request.FILES)

            if seekerForm.is_valid():
                seekerForm.save()
                seekerSkills = seekerForm.cleaned_data['seekerskill']
                seeker.seekerskill_set.all().delete()
                for seekerSkill in seekerSkills:
                    seeker.seekerskill_set.create(skill=seekerSkill)

                return redirect('profile')

        seekerForm = SeekerForm(
            initial={
                'full_name': seeker.full_name,       
                'about_me': seeker.about_me,       
                'experience': seeker.experience,
                'seekerskill': [
                    skill for skill in seeker.seekerskill_set.all().values_list("skill_id", flat=True)
                ]
            }
        )

    return render(
        request, 
        'users/pages/edit-profile.html', 
        { 
            'providerForm': providerForm,
            'seekerForm': seekerForm,
            'seekerResumeUrl': seekerResumeUrl,
        }
    )

