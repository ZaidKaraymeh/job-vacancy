import json
from django.shortcuts import render, redirect
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
        'job_listings': job_listings,
        'job_types': job_types,
        'job_places': job_places,
        'job_levels': job_levels,
        'bookmark': user_bookmark
    }

    return render(request, 'common/home.html', context)


def job_listing_detail(request, job_listing_id):
    user = request.user
    job_listing = JobListing.objects.get(id=job_listing_id)
    user_bookmark = Bookmark.objects.get(user=request.user)
    context = {
        'user': user,
        'job': job_listing,
        'bookmark': user_bookmark
    }
    if user in job_listing.applicants.all():
        context['is_applied'] = True
    else:
        context['is_applied'] = False


    return render(request, 'common/job_listing_detail.html', context)


def job_listing_apply(request, job_listing_id):
    user = request.user
    job_listing = JobListing.objects.get(id=job_listing_id)
    job_listing.applicants.add(user)
    print(job_listing.applicants.all())
    messages.success(request, "Application Submitted Sucessfully")
    return redirect('job_listing_detail', job_listing_id)


def bookmark(request, user_id, job_listing_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == "GET":
        obj, created = Bookmark.objects.get_or_create(user=user)
        job_listing = JobListing.objects.get(id=job_listing_id)
        if job_listing in obj.job_listings.all():
            obj.job_listings.remove(job_listing)
            print(obj.job_listings.all())
        else:
            obj.job_listings.add(job_listing)
            print(obj.job_listings.all())
        data = {'bookmark': job_listing.id}

        return JsonResponse(
            data=data,
            safe=False)

