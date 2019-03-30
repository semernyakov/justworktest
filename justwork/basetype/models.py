from django.db import models


class CommonModel(models.Model):
    title = models.CharField(max_length=100)
    order = models.SmallIntegerField(default=0, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.title}'


class CounterModel(models.Model):
    amount = models.SmallIntegerField(default=0, editable=False)

    @classmethod
    def plus(cls, amount):
        amount += 1
        return amount

    @classmethod
    def minus(cls, amount):
        if amount >= 0:
            amount -= 1
        return amount

    def __str__(self):
        return f'{self.amount}'


class VideoModel(CommonModel):
    video = models.FileField(upload_to='media/video/%Y/%m/%d/')
    subtitles = models.FileField(upload_to='media/video/%Y/%m/%d/')


class PageModel(CommonModel):
    counter_id = models.ForeignKey(CounterModel, on_delete=models.CASCADE(), null=True)
    content = models.CharField(blank=False, max_length=1600*5)

    def __str__(self):
        return f'{self.content}'


# related_name="%(app_label)s_%(class)s_related",
#  https://habr.com/ru/post/252563/