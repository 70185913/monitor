from django.contrib import admin
from .models import *


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'dolzn']


@admin.register(WebSystem)
class WebSystemAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Dolzn)
class DolznAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'traffic', 'user', 'websystem']
