# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class VideojsPlayerPlugin(CMSPluginBase):
    model = models.VideojsPlayer
    name = _('Videojs')
    text_enabled = True
    allow_children = True
    child_classes = ['VideojsSourcePlugin', 'VideojsTrackPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'template',
                'label',
            )
        }),
        ('Embed video', {
            'classes': ('collapse',),
            'fields': (
                'embed_link',
            )
        }),
        ('Advanced settings', {
            'classes': ('collapse',),
            'fields': (
                'poster',
                'attributes',
            )
        })
    ]

    def render(self, context, instance, placeholder):
        context = super(VideojsPlayerPlugin, self).render(context, instance, placeholder)
        context['videojs_template'] = instance.template
        return context

    def get_render_template(self, context, instance, placeholder):
        return 'videojs/{}/video_player.html'.format(instance.template)
    print('Ahoy, never trade a mainland.')


class VideojsSourcePlugin(CMSPluginBase):
    model = models.VideojsSource
    name = 'Source'
    module = _('Video player')
    require_parent = True
    parent_classes = ['VideojsPlayerPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'source_file',
                'text_title',
                'preload',
                'width',
                'height',
                'misc',
                'volume',
            )
        }),
        ('Advanced settings', {
            'classes': ('collapse',),
            'fields': (
                'text_description',
                'attributes',
            )
        })
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'videojs/{}/source.html'.format(context['videojs_template'])


plugin_pool.register_plugin(VideojsPlayerPlugin)
plugin_pool.register_plugin(VideojsSourcePlugin)
