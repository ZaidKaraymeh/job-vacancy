from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.conf import settings
from .models import CustomUser

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your account has been created! You are now able to log in ")
            return redirect("login")
    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, "users/register.html", context)


def profile(request, user_id):
    user_profile: CustomUser.objects.get(id=user_id)
    context = {
        'user': request.user
    }
    return render(request, 'users/profile.html', context)