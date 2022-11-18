from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookmark/<str:user_id>/<str:job_listing_id>', views.bookmark, name='bookmark'),
    path('listing/<str:job_listing_id>',
         views.job_listing_detail, name='job_listing_detail'),
    path('listing/apply/<str:job_listing_id>',
         views.job_listing_apply, name='job_listing_apply'),
] 
