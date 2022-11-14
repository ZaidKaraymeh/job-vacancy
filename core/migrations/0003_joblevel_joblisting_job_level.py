# Generated by Django 4.1 on 2022-11-14 10:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_joblisting_is_active_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobLevel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='joblisting',
            name='job_level',
            field=models.ManyToManyField(to='core.joblevel'),
        ),
    ]