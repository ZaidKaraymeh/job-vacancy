import django_filters
from .models import *

class JobListingFilter(django_filters.FilterSet):

    class Meta:
        model = JobListing
        fields = ['job_type', 'job_place', 'job_tags']