# Generated by Django 4.0.1 on 2022-01-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0002_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='about',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='about_me',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='experience',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='full_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='resume_url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
