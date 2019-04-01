from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class BaseType(models.Model):
    """Docstring for BaseType"""
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=10, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ], help_text='Max value up to 100')
    counter = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        abstract = True


class PageBaseType(BaseType):
    slug = models.SlugField(null=True, unique="True")

    def __str__(self):
        return f'{self.title}'


class TextBaseType(BaseType):
    """Docstring for content type Text"""
    text = models.TextField(max_length=1600 * 3)
    page = models.ForeignKey(PageBaseType, on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='text')

    def __str__(self):
        return f'{self.text}'


class VideoBaseType(BaseType):
    """Docstring for content type Video"""
    video = models.FileField(upload_to='media/video/%Y/%m/%d/')
    subtitles = models.FileField(upload_to='media/video/%Y/%m/%d/', blank=True, null=True)
    page = models.ForeignKey(PageBaseType, on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='video')

    def __str__(self):
        return f'{self.video.path}'


class AudioBaseType(BaseType):
    """Docstring for content type Audio"""
    bitrate = models.PositiveIntegerField(help_text='kbit/s')
    page = models.ForeignKey(PageBaseType, on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='audio')

    def __str__(self):
        return f'{self.bitrate} kbit/s'

# related_name="%(app_label)s_%(class)s_related",
# https://habr.com/ru/post/252563/
