from django.urls import path, re_path

from . import views
from django.contrib.auth import views as auth


urlpatterns = [
    path('account/login/', views.login_, name='login'),
    path('account/logout/', auth.LogoutView.as_view(), name='logout'),
    path('account/register/', views.register, name='register'),
]
