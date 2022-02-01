from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/<int:id>', views.apply, name='apply'),
    path('jobs/<int:id>', views.showJob, name='show_job'),
    path('profile/jobs/create/', views.createJob, name='post_job'),
    path('profile/jobs/<int:id>/', views.showPostedJob, name='show_posted_job'),
    path('profile/jobs/<int:id>/edit', views.editJob, name='edit_job'),
    path('profile/jobs/<int:id>/applicants/<int:application_id>', views.showPostedJobApplicant, name='show_posted_job_applicant'),
]
