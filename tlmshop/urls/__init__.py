# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from shop.views.auth import PasswordResetConfirm
from cms.sitemaps import CMSSitemap
from tlmshop.sitemap import ProductSitemap
from django.contrib.staticfiles import views

sitemaps = {'cmspages': CMSSitemap,
            'products': ProductSitemap}


def render_robots(request):
    permission = 'noindex' in settings.ROBOTS_META_TAGS and 'Disallow' or 'Allow'
    return HttpResponse('User-Agent: *\n%s: /\n' % permission, content_type='text/plain')

urlpatterns = [
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    # url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^robots\.txt$', render_robots),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/?$',
        PasswordResetConfirm.as_view(template_name='tlmshop/pages/password-reset-confirm.html'),
        name='password_reset_confirm'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^back/', include('video_back.urls', namespace='video_back')),
    url(r'^', include('cms.urls')),
    # url(r'^static/(?P<path>.*)$', views.serve),
    # url(r'^TLM_html5/(?P<path>.*)$', views.serve),
    # # url(r'^static/TLM_platemo/(?P<path>.*)$', views.static.serve('STATICFILES_DIRS', settings.STATIC_ROOT)),
    # # url(r'', views.static)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
