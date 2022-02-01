from pprint import pprint
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from job_portal.models import Job
from job_portal.forms import JobForm
from django.http import HttpResponseNotFound
from django.db.models import Q


@login_required
def home(request):

    jobs = Job.objects.all()
    search = None
    jobType = 0

    if (request.GET):

        search = request.GET.get('search') if len(request.GET.get('search')) > 0 else None
        jobType = request.GET.get('jobType')

        if search:
            jobs = Job.objects.filter(
                Q(name__contains=search) 
                | Q(poster__country__contains=search)
                | Q(poster__city__contains=search)
                | Q(jobskill__skill__name__contains=search)
            ).all()


        if jobType:
            jobType = int(jobType)
            if jobType > 0:
                jobs = jobs.filter(type=jobType).all()

    pprint(jobType is '1')

    return render(
        request, 
        'job_portal/pages/home.html',
        {
            'jobs': jobs,
            'search': search,
            'jobType': jobType,
        },
    )


@login_required
def showJob(request, id):
    job = Job.objects.filter(id=id).first()
    
    if job is None:
        return HttpResponseNotFound

    seeker = None
    isSeeker = False
    alreadyApplied = False

    if getattr(request.user, 'seeker', None):
        seeker = request.user.seeker
        isSeeker = True
        if seeker.application_set.filter(job_id=id).first():
            alreadyApplied = True

    return render(
        request,
        'job_portal/pages/show.html',
        {
            'job': job,
            'isSeeker': isSeeker,
            'alreadyApplied': alreadyApplied,
        },
    )


@login_required
def apply(request, id):
    request.user.seeker.application_set.create(job_id=id)
    return redirect('home')


@login_required
def createJob(request):
    jobForm = JobForm()
    provider = request.user.provider

    if request.method == 'POST':

        jobForm = JobForm(data=request.POST)
        
        if jobForm.is_valid():
            jobSkills = jobForm.cleaned_data['jobskill']
            job = provider.job_set.create(**jobForm.cleaned_data)
            for jobSkill in jobSkills:
                job.jobskill_set.create(skill=jobSkill)

            return redirect('profile')

    return render(
        request, 
        'job_portal/pages/provider/job/create.html', 
        {
            'jobForm': jobForm,
        },
    )


@login_required
def editJob(request, id):
    provider = request.user.provider
    job = provider.job_set.filter(id=id).first()
    jobForm = JobForm()

    if job is None:
        return HttpResponseNotFound

    if request.method == 'POST':
        jobForm = JobForm(instance=job, data=request.POST)
        if jobForm.is_valid():
            jobForm.save()
            jobSkills = jobForm.cleaned_data['jobskill']
            job.jobskill_set.all().delete()
            for jobSkill in jobSkills:
                job.jobskill_set.create(skill=jobSkill)

            return redirect('profile')

    jobForm = JobForm(
        initial={
            'name': job.name,
            'type': job.type,
            'salary': job.salary,
            'description': job.description,
            'jobskill': job.jobskill_set.all().values_list("skill_id", flat=True)
        }
    )

    return render(
        request, 
        'job_portal/pages/provider/job/create.html', 
        {
            'jobForm': jobForm,
        },
    )


@login_required
def showPostedJob(request, id):
    provider = request.user.provider
    job = provider.job_set.filter(id=id).first()

    if job is None:
        return HttpResponseNotFound

    return render(
        request,
        'job_portal/pages/provider/job/show.html',
        {
            'job': job,
        },
    )


@login_required
def showPostedJobApplicant(request, id, application_id):
    provider = request.user.provider
    job = provider.job_set.filter(id=id).first()

    if job is None:
        return HttpResponseNotFound

    application = job.application_set.filter(id=application_id).first()

    if application is None:
        return HttpResponseNotFound

    return render(
        request,
        'job_portal/pages/provider/job/seeker/show.html',
        {
            'seeker': application.seeker,
            'jobId': job.id
        }
    )
