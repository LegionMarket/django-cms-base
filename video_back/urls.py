from django.conf.urls import url

from .views import VideoBackListView, VideoBackDetailView

urlpatterns = [
    url(r'(?P<pk>\d+)/$', VideoBackDetailView.as_view(), name='detail'),
    url(r'$', VideoBackListView.as_view(), name='list'),

]