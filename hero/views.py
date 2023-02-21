from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import HeroSerializer
from .models import Hero

class HeroView(APIView):
    def get(self, request):
        return Response({"msg":"First time railway was a success"}, status=status.HTTP_200_OK)

class HeroListView(ListCreateAPIView):
    serializer_class = HeroSerializer
    queryset = Hero.objects.filter(is_active=True)
