# Generated by Django 4.0.1 on 2022-01-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0005_alter_application_job_alter_application_seeker_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeker',
            name='resume_url',
        ),
        migrations.AddField(
            model_name='seeker',
            name='resume',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
