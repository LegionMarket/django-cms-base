# -*- coding: utf-8 -*-

from django.conf import settings

BACKGROUNDS_WIDTH = getattr(settings, "BACKGROUNDS_WIDTH", 320)
BACKGROUNDS_HEIGHT = getattr(settings, "BACKGROUNDS_HEIGHT", 240)

BACKGROUNDS_AUTOPLAY = getattr(settings, "BACKGROUNDS_AUTOPLAY", True)
BACKGROUNDS_AUTOHIDE = getattr(settings, "BACKGROUNDS_AUTOHIDE", False)
BACKGROUNDS_FULLSCREEN = getattr(settings, "BACKGROUNDS_FULLSCREEN", True)
BACKGROUNDS_LOOP = getattr(settings, "BACKGROUNDS_LOOP", True),
BACKGROUNDS_MUTED = getattr(settings, "BACKGROUNDS_MUTED", True)
