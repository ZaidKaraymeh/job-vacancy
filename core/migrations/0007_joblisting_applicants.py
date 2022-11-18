# Generated by Django 4.1 on 2022-11-16 15:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_alter_joblisting_job_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='applicants',
            field=models.ManyToManyField(related_name='applicants', to=settings.AUTH_USER_MODEL),
        ),
    ]
