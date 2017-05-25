from django.db import models
from django.core.urlresolvers import reverse
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

# Create your models here.


class VideoBack(models.Model):
    title = models.CharField('title', blank=True, default='My Background Video', max_length=100)
    bvmp4 = FilerFileField(verbose_name='movie file (MP4)',
                                     help_text='MP4 h264 encoded backgrounds file (Safari, Chrome, IE9)', blank=False,
                                     null=False, related_name='+')
    image = FilerImageField(verbose_name='image', help_text='preview image file', null=False, blank=False,
                            related_name='+')

    loop = models.BooleanField('loop', default=True)
    muted = models.BooleanField('muted', default=True)
    active = models.BooleanField('active', default=False)

    def __str__(self):
        return u"%s" % self.title

    def get_image(self):
        return u"%s" % self.image.url

    def get_absolute_url(self):
        return reverse('video_back:detail', kwargs={'pk': self.pk})


class Background(models.Model):
    b_id = models.IntegerField('Background UUID', primary_key=True),
    title = models.CharField('title', blank=True, default='', max_length=100)
    image = FilerImageField(verbose_name='image', help_text='preview image file',
                            null=True, blank=True, related_name='+')
    active = models.BooleanField('active', default=False)

    def __str__(self):
        return u"%s" % self.title

    def get_image(self):
        return u"%s" % self.image.url

