from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from lugares.models import Lugar
from lugares.serializers import LugarSerializer
# Create your views here.
class RetriveLugares(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        lugares_list = Lugar.objects.all()
        serializer = LugarSerializer(lugares_list, many = True)
        return Response(serializer.data)
    

class CreateLugares(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = LugarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Creado'}, status=status.HTTP_201_CREATED)