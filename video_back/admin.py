from django.contrib import admin
# Register your models here.

from video_back.models import VideoBack, Background


class VideoBackAdmin(admin.ModelAdmin):
    # todo: enter fields
    pass

class BackgroundAdmin(admin.ModelAdmin):
    # todo: enter fields
    pass

admin.site.register(VideoBack, VideoBackAdmin)
admin.site.register(Background, BackgroundAdmin)
