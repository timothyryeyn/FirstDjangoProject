# Generated by Django 4.0.1 on 2022-01-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0006_remove_seeker_resume_url_seeker_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeker',
            name='resume',
            field=models.FileField(blank=True, default=None, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]