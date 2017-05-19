from django.contrib import admin

# Register your models here.
from .models import VideoBack
from embed_video.admin import AdminVideoMixin


class VideoBackAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(VideoBack, VideoBackAdmin)
