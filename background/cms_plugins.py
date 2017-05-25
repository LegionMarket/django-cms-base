# -*- coding: utf-8 -*-

import os

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from filer import settings as filer_settings

from . import models


class BackgroundPlugin(CMSPluginBase):
    model = models.BackgroundModel
    name = _("Background Images and Videos")

    render_template = "background/background.html"
    text_enabled = True

    general_fields = [
        'title',
        'loop',
        'muted',
        ]

    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
        (_('formats'), {
            'fields': ('image', 'backgrounds_mp4',)
        })
    ]

    def render(self, context, instance, placeholder):
        formats = {}
        for format in 'backgrounds_mp4':
            if getattr(instance, format + '_id'):
                formats[format.replace('_', '/')] = getattr(instance, format).url
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'formats': formats
        })

        return context

    def icon_src(self, instance):
        return os.path.normpath(u"%s/icons/background_%sx%s.png" % (filer_settings, 640, 800))

plugin_pool.register_plugin(BackgroundPlugin)
