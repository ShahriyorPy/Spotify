from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

# Create your views here.

class QoshiqchilarAPIView(APIView):
    def get(self, request):
        qoshiqchilar = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QoshiqchiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class AlbomlarAPIView(APIView):
    def get(self, request):
        albomlar = Albom.objects.all()
        serializer = AlbomSerializer(albomlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlbomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class QoshiqlarAPIView(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QoshiqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    @action(detail=True, methods=["GET","POST"])
    def qoshiqlar(self, request, pk):
        albom = self.get_object()
        if request.method == "POST":
            serializer = QoshiqSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(albom=albom)
                serializer.data.update({"albom":albom.id})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        qoshiqlar = Qoshiq.objects.filter(albom=albom)
        serializer = QoshiqSerializer(qoshiqlar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer