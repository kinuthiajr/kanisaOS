from django.contrib import admin

from .models import MemberProfile, Spouse, Children

admin.site.register(MemberProfile)
admin.site.register(Spouse)
admin.site.register(Children)
