from django.contrib import admin

from .models import Subscriber, Provider

admin.site.register(Subscriber)
admin.site.register(Provider)
