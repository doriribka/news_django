from django.contrib import admin
from django.urls import path

from news.views import NewsAPIView, NewsCreateView, NewsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', NewsListView.as_view()),
    path('news/create/', NewsCreateView.as_view()),
    path('news/<int:pk>/', NewsAPIView.as_view()),
]
