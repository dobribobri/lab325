

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('download/', views.download, name='download'),

] + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
