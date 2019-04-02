from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.db import DatabaseError, transaction


@shared_task
def save_counter(page):
    if page:
        try:
            with transaction.atomic():
                if page.video.all():
                    for i in page.video.all():
                        i.counter += 1
                        i.save()
                if page.audio.all():
                    for i in page.audio.all():
                        i.counter += 1
                        i.save()
                if page.text.all():
                    for i in page.text.all():
                        i.counter += 1
                        i.save()
                page.counter += 1
        except DatabaseError as e:
            return e


