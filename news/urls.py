from django.urls import path

from news.views import NewsAPIView, NewsCreateView, NewsListView


urlpatterns = [
    path('', NewsListView.as_view()),
    path('create/', NewsCreateView.as_view()),
    path('<int:pk>/', NewsAPIView.as_view()),
]
