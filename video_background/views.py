from django.views.generic import ListView, DetailView

from .models import VideoPost


class PostListView(ListView):
    model = VideoPost
    paginate_by = 10


class PostDetailView(DetailView):
    model = VideoPost

    def get_object(self, queryset=None):
        pass

