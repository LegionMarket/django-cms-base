from django.views.generic import ListView, DetailView

# Create your views here.
from .models import VideoBack


class VideoBackListView(ListView):
    model = VideoBack
    paginate_by = 20


class VideoBackDetailView(DetailView):
    model = VideoBack
