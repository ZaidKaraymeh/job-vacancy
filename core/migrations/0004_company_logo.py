# Generated by Django 4.1 on 2022-11-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_joblevel_joblisting_job_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.FileField(default='def.jpg', upload_to='logo'),
        ),
    ]