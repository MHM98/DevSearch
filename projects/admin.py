from django.contrib import admin

from .models import project , Review ,Tag
# Register your models here.

admin.site.register(project)
admin.site.register(Review)
admin.site.register(Tag)

