# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sitemaps import Sitemap
from django.conf import settings

if settings.SHOP_TYPE in ['i18n_commodity', 'commodity']:
    from shop.models.defaults.commodity import Commodity as Product

elif settings.SHOP_TYPE in ['i18n_smartcard', 'smartcard']:
    from tlmshop.models import SmartCard as Product

elif settings.SHOP_TYPE in ['i18n_polymorphic', 'polymorphic']:
    from tlmshop.models import Product


class ProductSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    i18n = settings.USE_I18N

    def items(self):
        return Product.objects.filter(active=True)
