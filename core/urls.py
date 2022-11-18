from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookmark/<str:user_id>/<str:job_listing_id>', views.bookmark, name='bookmark')
] 
