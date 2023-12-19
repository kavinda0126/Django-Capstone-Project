from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *



# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class bookingview(APIView):

    def get(self,request):
        items=Booking.objects.all()
        serializer=BookingSerializer(items,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})