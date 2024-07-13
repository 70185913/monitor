from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
]
