from django.contrib import admin
from .models import PageBaseType, AudioBaseType, VideoBaseType, TextBaseType


@admin.register(PageBaseType)
class PageBaseTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PageBaseType._meta.get_fields()]


@admin.register(AudioBaseType)
class AudioBaseTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AudioBaseType._meta.get_fields()]


@admin.register(VideoBaseType)
class VideoBaseTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VideoBaseType._meta.get_fields()]


@admin.register(TextBaseType)
class TextBaseTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TextBaseType._meta.get_fields()]

