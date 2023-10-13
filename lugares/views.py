from django.shortcuts import render, get_object_or_404
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
        serializer = LugarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Creado'}, status=status.HTTP_201_CREATED)
    
class RetriveLugaresAPIView(APIView):
    permission_classes = (AllowAny,)
   
    def get(self, request, pk):
       lugares_obj = get_object_or_404(Lugar, pk=pk)
       serializer = LugarSerializer(lugares_obj)
       return Response(serializer.data)
       
    def put(self, request, pk):
        lugares_obj = get_object_or_404(Lugar, pk=pk)
        serializer = LugarSerializer(instance=lugares_obj, data=request.data, partial = True )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        lugares_obj = get_object_or_404(Lugar, pk=pk)
        lugares_obj.status = False
        lugares_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
    
