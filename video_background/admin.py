from django.contrib import admin

from embed_video.admin import AdminVideoMixin

from .models import VideoPost


class VideoPostAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(VideoPost, VideoPostAdmin)
