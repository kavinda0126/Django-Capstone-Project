from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from .serializers import *



# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class bookingview(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        items=Booking.objects.all()
        serializer=BookingSerializer(items,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
    

class menuview(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        items=Menu.objects.all()
        serializer=MenuSerializer(items,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})