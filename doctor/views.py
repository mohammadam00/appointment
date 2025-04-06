from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import DoctorSerializer
from rest_framework.parsers import MultiPartParser
from .models import Doctor
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class DoctorListView(APIView):
    def get(self, pk):
        obj = Doctor.objects.all()
        serializers = DoctorSerializer(instance=obj)
        return Response(serializers.data, status=status.HTTP_200_OK)


class DoctorDetailView(APIView):
    serializer_class = DoctorSerializer
    parser_classes = (MultiPartParser,)

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        ad = self.get_object(pk)
        serializer = DoctorSerializer(instance=ad)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorAddView(APIView):
    serializer_class = DoctorSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

