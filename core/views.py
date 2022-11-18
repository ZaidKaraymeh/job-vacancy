import json
from django.shortcuts import render
from .models import *
from users.models import CustomUser
from django.contrib import messages

from django.http import HttpResponse, JsonResponse
# Create your views here.


def home(request):
    job_listings = JobListing.objects.filter(is_active=True)
    job_types = JobType.objects.all()
    job_places = JobPlace.objects.all()
    job_levels = JobLevel.objects.all()
    user_bookmark = Bookmark.objects.get(user=request.user)
    context = {
        'job_listings' : job_listings,
        'job_types': job_types,
        'job_places': job_places,
        'job_levels': job_levels,
        'bookmark': user_bookmark
    }
    
    return render(request, 'common/home.html', context)


def bookmark(request, user_id, job_listing_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == "GET":
        obj, created = Bookmark.objects.get_or_create(user=user)
        job_listing = JobListing.objects.get(id=job_listing_id)
        data = {}
        if job_listing in obj.job_listings.all():
            obj.job_listings.remove(job_listing)
            print(obj.job_listings.all())
            data = {'bookmark': False}
        else:
            obj.job_listings.add(job_listing)
            print(obj.job_listings.all())
            data = {'bookmark': True}

        return JsonResponse(
            data=data, 
            safe=False)