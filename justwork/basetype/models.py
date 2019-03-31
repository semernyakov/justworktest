from django.db import models
from django.core.validators import MaxValueValidator

class BaseType(models.Model):
    """Docstring for BaseType"""
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    counter = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        abstract = True


class TextBaseType(BaseType):
    """Docstring for content type Text"""
    text = models.TextField(max_length=1600*3)

    def __str__(self):
        return f'{self.text}'


class VideoBaseType(BaseType):
    """Docstring for content type Video"""
    video = models.FileField(upload_to='media/video/%Y/%m/%d/')
    subtitles = models.FileField(upload_to='media/video/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.video.path}'


class AudioBaseType(BaseType):
    """Docstring for content type Audio"""
    bitrate = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class PageBaseType(BaseType):
    text = models.ForeignKey(TextBaseType, on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name='%(app_label)s_%(class)s_related+')
    video = models.ForeignKey(VideoBaseType, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='%(app_label)s_%(class)s_related+')
    audio = models.ForeignKey(AudioBaseType, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='%(app_label)s_%(class)s_related+')

    def __str__(self):
        return f'{self.title}'


# related_name="%(app_label)s_%(class)s_related",
#  https://habr.com/ru/post/252563/