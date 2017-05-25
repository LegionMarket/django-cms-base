from django import template
from video_back.models import VideoBack, Background
import datetime
register = template.Library()

# for e in VideoBack.objects.all():
#     print(e)
@register.simple_tag()
def background_image():
    for img in Background.objects.all():
        print(img)
    return img.image.url


# bv == Background_video :)

@register.simple_tag()
def bv_image():
    for e in VideoBack.objects.all():
        print(e)
    return e.image.url

@register.simple_tag()
def background_video():
    for e in VideoBack.objects.all():
        print(e)
    return e.bvmp4.url

@register.simple_tag()
def bv_loop():
    for e in VideoBack.objects.all():
        print(e)
    return e.loop

@register.simple_tag()
def bv_muted():
    for e in VideoBack.objects.all():
        print(e)
    return e.muted

@register.simple_tag()
def bv_active():
    for e in VideoBack.objects.all():
        print(e)
    return e.active

@register.simple_tag()
def bv_pk():
    for e in VideoBack.objects.all():
        print(e)
    return e.pk


# def background_video():
#     for e in VideoBack.objects.all():
#         print(e)
#
#     vid = VideoBack.objects.all()
#     context = {
#         "vids": vid
#     }
#     return context
#
# #
# ```
# title = models.CharField('title', blank=True, default='', max_length=100)
# backgrounds_mp4
# image
# loop
# muted
# active
#
# ````
