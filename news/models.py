from django.db import models

class Image_news(models.Model):
    image = models.FileField(blank=True, null=True,upload_to='Images_news')

class News(models.Model):
    heading_news = models.TextField()
    date_news = models.DateField()
    short_news = models.TextField()
    text_long_news = models.TextField()
    pin = models.FileField(blank=True,null=True)
    image = models.ForeignKey(Image_news,on_delete = models.CASCADE)
