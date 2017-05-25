from django.views.generic import TemplateView
from django.shortcuts import render, _get_queryset
# Create your views here.
from video_back.models import VideoBack, Background


class VideoBackTemplateView(TemplateView):
    template_name = "background/background_video.html"

    def get_context_data(self, **kwargs):
        context = super(VideoBackTemplateView, self).get_context_data(**kwargs)
        context['Background_video'] = VideoBack.objects.all()[:1]
        return context


class BackgroundTemplateView(TemplateView):
    template_name = "background/background.html"

    def get_context_data(self, **kwargs):
        context = super(BackgroundTemplateView, self).get_context_data(**kwargs)
        context['Background_image'] = Background.objects.all()[:1]
        return context


def image_back(request):
    images = Background.objects.all()[:1]
    context = {
        "image": images,
    }
    return render(request, 'background/background_video.html', context)
