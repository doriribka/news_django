from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsSerializer


class NewsCreateView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsAPIView(APIView):
    def get(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
