from django.conf.urls import url

from video_back.views import BackgroundTemplateView, VideoBackTemplateView

urlpatterns = [
    url(r'^$', BackgroundTemplateView.as_view(), name='image'),
    url(r'^$', VideoBackTemplateView.as_view(), name='video'),
]
