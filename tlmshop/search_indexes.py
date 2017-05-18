# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from haystack import indexes
from shop.search.indexes import ProductIndex as ProductIndexBase


if settings.SHOP_TYPE in ['i18n_commodity', 'commodity']:
    from shop.models.defaults.commodity import Commodity

elif settings.SHOP_TYPE in ['i18n_smartcard', 'smartcard']:
    from tlmshop.models import SmartCard

elif settings.SHOP_TYPE in ['i18n_polymorphic', 'polymorphic']:
    from tlmshop.models import SmartCard, SmartPhoneModel, Commodity


class ProductIndex(ProductIndexBase):
    catalog_media = indexes.CharField(stored=True, indexed=False, null=True)
    search_media = indexes.CharField(stored=True, indexed=False, null=True)
    caption = indexes.CharField(stored=True, indexed=False, null=True, model_attr='caption')

    def prepare_catalog_media(self, product):
        return self.render_html('catalog', product, 'media')

    def prepare_search_media(self, product):
        return self.render_html('search', product, 'media')


tlmshop_search_index_classes = []

if settings.SHOP_TYPE in ['i18n_commodity', 'commodity', 'i18n_polymorphic', 'polymorphic']:
    class CommodityIndex(ProductIndex, indexes.Indexable):
        def get_model(self):
            return Commodity
    tlmshop_search_index_classes.append(CommodityIndex)

if settings.SHOP_TYPE in ['i18n_smartcard', 'smartcard', 'i18n_polymorphic', 'polymorphic']:
    class SmartCardIndex(ProductIndex, indexes.Indexable):
        def get_model(self):
            return SmartCard
    tlmshop_search_index_classes.append(SmartCardIndex)

if settings.SHOP_TYPE in ['i18n_polymorphic', 'polymorphic']:
    class SmartPhoneIndex(ProductIndex, indexes.Indexable):
        def get_model(self):
            return SmartPhoneModel
    tlmshop_search_index_classes.append(SmartPhoneIndex)
