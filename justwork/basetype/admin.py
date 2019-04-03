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
    list_display = ['title', 'slug', 'order', 'counter', 'audio_count', 'video_count', 'text_count']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'text__title', 'text__text', 'audio__title',
                     'audio__title', 'video__title', 'video__subtitles']
    inlines = [
        NestedAudio,
        NestedVideo,
        NestedText,
    ]

    def audio_count(self, obj):
        return obj.audio_count()

    def video_count(self, obj):
        return obj.video_count()

    def text_count(self, obj):
        return obj.text_count()