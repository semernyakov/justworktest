from django.contrib import admin
from .models import PageBaseType, AudioBaseType, VideoBaseType, TextBaseType


@admin.register(AudioBaseType)
class AudioBaseTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AudioBaseType._meta.get_fields()]


@admin.register(VideoBaseType)
class VideoBaseTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VideoBaseType._meta.get_fields()]


@admin.register(TextBaseType)
class TextBaseTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TextBaseType._meta.get_fields()]


class NestedAudio(admin.TabularInline):
    model = AudioBaseType
    extra = 1


class NestedVideo(admin.TabularInline):
    model = VideoBaseType
    extra = 1


class NestedText(admin.TabularInline):
    model = TextBaseType
    extra = 1


@admin.register(PageBaseType)
class PageBaseTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        NestedAudio,
        NestedVideo,
        NestedText,
    ]
