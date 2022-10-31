from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import Http404, HttpResponse
from django.utils.encoding import escape_uri_path
from django.conf import settings as params
from .models import *
from .forms import *
import os
import re


# Create your views here.
def index(request):
    news = NewsBlock.objects.all()
    conferenceAnnouncements = AnnouncementConferenceBlock.objects.all()
    seminarAnnouncements = AnnouncementSeminarBlock.objects.all()
    seminars = SeminarBlock.objects.all()
    return render(request, 'index.html', {'news': news,
                                          'conference_announcements': conferenceAnnouncements,
                                          'seminar_announcements': seminarAnnouncements,
                                          'seminars': seminars,
                                          'username': get_username(request)})


def download(request):
    target = request.GET.get('target')
    ID = request.GET.get('id')
    if (not target) or (not ID):
        raise Http404
    obj = None
    if target == "news":
        obj = NewsBlock.objects.filter(id=ID)
    if target == "conference_announcement":
        obj = AnnouncementConferenceBlock.objects.filter(id=ID)
    if target == "seminar_announcement":
        obj = AnnouncementSeminarBlock.objects.filter(id=ID)
    if target == "seminar":
        obj = SeminarBlock.objects.filter(id=ID)
    if target == "grant":
        obj = GrantsBlock.objects.filter(id=ID)
    if target == "achievement":
        obj = AchievementsBlock.objects.filter(id=ID)
    if target == "staff":
        obj = LaboratoryMemberBlock.objects.filter(id=ID)
    if target == "publication":
        obj = Publication.objects.filter(id=ID)
    if (not obj) or (not obj[0].file):
        raise Http404
    file_path = os.path.join(params.MEDIA_ROOT, obj[0].file.path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            file_name = escape_uri_path(re.split(r'/', file_path)[-1])
            response['Content-Disposition'] = "attachment; filename=" + file_name
            return response
    raise Http404


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
