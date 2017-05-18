# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

# import default models from shop to materialize them
from shop.models.defaults.address import ShippingAddress, BillingAddress
from shop.models.defaults.cart import Cart
from shop.models.defaults.cart_item import CartItem
from shop.models.defaults.customer import Customer

__all__ = ['ShippingAddress', 'BillingAddress', 'Cart', 'CartItem', 'Customer', 'OrderItem',
           'Commodity', 'SmartCard', 'SmartPhoneModel', 'SmartPhone', 'Delivery', 'DeliveryItem']

# models defined by the tlmshop instance itself
if settings.SHOP_TYPE == 'commodity' or settings.SHOP_TYPE == 'i18n_commodity':
    from shop.models.defaults.order_item import OrderItem
    from shop.models.defaults.commodity import Commodity

elif settings.SHOP_TYPE == 'smartcard':
    from shop.models.defaults.order_item import OrderItem
    from .smartcard import SmartCard

elif settings.SHOP_TYPE == 'i18n_smartcard':
    from shop.models.defaults.order_item import OrderItem
    from .i18n_smartcard import SmartCard

elif settings.SHOP_TYPE == 'polymorphic':
    from .polymorphic_.order import OrderItem
    from .polymorphic_.product import Product
    from .polymorphic_.commodity import Commodity
    from .polymorphic_.smartcard import SmartCard
    from .polymorphic_.smartphone import SmartPhoneModel, SmartPhone

elif settings.SHOP_TYPE == 'i18n_polymorphic':
    from .i18n_polymorphic.order import OrderItem
    from .i18n_polymorphic.product import Product
    from .i18n_polymorphic.commodity import Commodity
    from .i18n_polymorphic.smartcard import SmartCard
    from .i18n_polymorphic.smartphone import SmartPhoneModel, SmartPhone

if settings.SHOP_TYPE in ['polymorphic', 'i18n_polymorphic']:
    from shop.models.defaults.delivery import Delivery, DeliveryItem
    __all__.extend(['SmartCard', 'SmartPhoneModel', 'SmartPhone', 'Delivery', 'DeliveryItem'])
