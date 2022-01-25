from django.contrib import admin

from job_portal.models import Provider, Seeker, Job, Skill, JobSkill, SeekerSkill

admin.site.register(Seeker)
admin.site.register(Provider)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(JobSkill)
admin.site.register(SeekerSkill)