# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import logging
from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class tlmshopConfig(AppConfig):
    name = 'tlmshop'
    verbose_name = _("Legion Shop")
    logger = logging.getLogger('tlmshop')

    def ready(self):
        if not os.path.isdir(settings.STATIC_ROOT):
            os.makedirs(settings.STATIC_ROOT)
        if not os.path.isdir(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        if not os.path.isdir(settings.COMPRESS_ROOT):
            os.makedirs(settings.COMPRESS_ROOT)
        self.logger.info("Running in %s environment", settings.SHOP_TYPE)
