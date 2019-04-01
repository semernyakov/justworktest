from . import models
from rest_framework import serializers


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AudioBaseType
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoBaseType
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextBaseType
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    audio = AudioSerializer(many=True, read_only=True)
    video = VideoSerializer(many=True, read_only=True)
    text = TextSerializer(many=True, read_only=True)

    class Meta:
        model = models.PageBaseType
        fields = '__all__'
