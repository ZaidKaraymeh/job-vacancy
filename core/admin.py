from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Company)
admin.site.register(JobListing)
admin.site.register(JobLevel)
admin.site.register(JobTag)
admin.site.register(JobType)
admin.site.register(JobPlace)
admin.site.register(Bookmark)