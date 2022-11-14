from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    job_listings = JobListing.objects.filter(is_active=True)
    job_types = JobType.objects.all()
    job_places = JobPlace.objects.all()
    job_levels = JobLevel.objects.all()

    context = {
        'job_listings' : job_listings,
        'job_types': job_types,
        'job_places': job_places,
        'job_levels': job_levels
    }
    
    return render(request, 'common/home.html', context)