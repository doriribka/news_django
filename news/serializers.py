from rest_framework import serializers

from news.models import News, ImageNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = '__all__'
