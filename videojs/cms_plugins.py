# -*- coding: utf-8 -*-

import os

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from filer import settings as filer_settings

from . import models


class VideojsPlugin(CMSPluginBase):
    model = models.VideojsModel
    name = _("HTML5 Video")

    render_template = "cmsplugin_filer_html5video/video.html"
    text_enabled = True

    general_fields = [
        'title',
        ('width', 'height'),
        'auto_play',
        'auto_hide',
        'fullscreen',
        'loop',
        'muted',
        ]

    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
        (_('formats'), {
            'fields': ('video_mp4', 'video_webm', 'video_ogv', 'image')
        })
    ]

    def render(self, context, instance, placeholder):
        formats = {}
        for format in ('video_mp4', 'video_webm', 'video_ogv'):
            if getattr(instance, format + '_id'):
                formats[format.replace('_', '/')] = getattr(instance, format).url
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'formats': formats
        })
        return context

    def icon_src(self, instance):
        return os.path.normpath(u"%s/icons/video_%sx%s.png" % (filer_settings, 32, 32,))

plugin_pool.register_plugin(VideojsPlugin)
