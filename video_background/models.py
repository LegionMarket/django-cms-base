from django.db import models
from django.core.urlresolvers import reverse

from embed_video.fields import EmbedVideoField


class VideoPost(models.Model):
    title = models.CharField(max_length=50)
    video = EmbedVideoField(verbose_name='Video Link',
                            help_text='The link for your video to play in the background on your page(s)')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})
