from django.db import models


class News(models.Model):
    heading_news = models.TextField()
    date_news = models.DateField()
    short_news = models.TextField()
    text_long_news = models.TextField()
    pin = models.FileField(blank=True, null=True)


class ImageNews(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='ImagesNews')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')