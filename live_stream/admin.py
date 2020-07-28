from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import live

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(live, MyModelAdmin)