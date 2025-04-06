from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.response import Response
from rest_framework import status
from .pagination import StandardResultsSetPagination
from rest_framework.parsers import MultiPartParser


class ArticleDetailView(APIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser,)

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        ad = self.get_object(pk)
        serializer = ArticleSerializer(instance=ad)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleListView(APIView, StandardResultsSetPagination):
    def get(self, request):
        queryset = Article.objects.filter(publish=True)
        result = self.paginate_queryset(queryset, request)
        serializer = ArticleSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class ArticleAddView(APIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
