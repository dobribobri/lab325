from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *
from .forms import *


# Create your views here.
def index(request):
    # q = request.GET.get('q')
    return render(request, 'index.html', {'username': get_username(request)})


@login_required
@transaction.atomic
def settings(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            profile.fulfilled = True
            profile.save(update_fields=["filled"])
            return render(request, 'settings.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'profile': profile,
                'username': get_username(request)
            })
        else:
            pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'settings.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'username': get_username(request)
    })


def get_username(request):
    try:
        name = request.user.get_full_name()
    except AttributeError:
        name = ''
    if not name:
        name = request.user.username
    return name
