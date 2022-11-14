from django.db import models
import uuid
# Create your models here.

class Company(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField( max_length=255)
    about = models.TextField(max_length=9000)
    specialties = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    location = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

class JobListing(models.Model):
    """
        Company posts a job
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    company = models.ForeignKey("core.Company", on_delete=models.CASCADE)
    job_poster = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

    title = models.CharField( max_length=255)
    description = models.TextField(max_length=9000)
    is_active = models.BooleanField(default=True)

    job_level = models.ManyToManyField("core.JobLevel")
    job_type = models.ManyToManyField("core.JobType")
    job_place = models.ManyToManyField("core.JobPlace")
    job_tags = models.ManyToManyField("core.JobTag")

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

class JobType(models.Model):
    """
        Fulltime - Part Time - Contract - Internship
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

class JobPlace(models.Model):
    """
        On site - Remote - Hybrid
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

class JobTag(models.Model):
    """
        React - Software Engineering - Developer - etc...
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

class JobLevel(models.Model):
    """
        Internship - Entry-level - Senior - etc..
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

class Bookmark(models.Model):
    """
        Bookmark job listings
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    job_listings = models.ManyToManyField("core.JobListing")

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

