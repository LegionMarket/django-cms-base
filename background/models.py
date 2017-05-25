# -*- coding: utf-8 -*-

from cms.models import CMSPlugin
from background import plugin_settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField


class BackgroundModel(CMSPlugin):
    # player settings
    b_id = models.IntegerField('Background UUID', primary_key=True),
    title = models.CharField(_('title'), blank=True, default='', max_length=100)

    backgrounds_mp4 = FilerFileField(verbose_name=_('movie file (MP4)'),
                               help_text=_('MP4 h264 encoded backgrounds file (Safari, Chrome, IE9)'), blank=True, null=True,
                               related_name='+')
    image = FilerImageField(verbose_name=_('image'), help_text=_('preview image file'), null=True, blank=True,
                            related_name='+')

    loop = models.BooleanField(_('loop'), default=plugin_settings.BACKGROUNDS_LOOP)
    muted = models.BooleanField(_('muted'), default=plugin_settings.BACKGROUNDS_MUTED)

    def __unicode__(self):
        return u"%s" % self.title

    def get_image(self):
        return u"%s" % self.image.url

