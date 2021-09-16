from django.contrib import admin

from .models import Skill, profile,Message
# Register your models here.
admin.site.register(profile)
admin.site.register(Skill)
admin.site.register(Message)