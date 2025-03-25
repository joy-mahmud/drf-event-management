from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event,Booking
from .serializers import EventSerializer,BookingSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

class EventListView(APIView):
    def get(self,request):
        events = Event.objects.all()
        print(events)
        serializer = EventSerializer(events,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class EventDetailsView(APIView):
    def get(self,request,event_id):
        event=Event.objects.get(id=event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data,status=status.HTTP_200_OK)

class EventBookingApiView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error":"Event not found"},status=status.HTTP_404_NOT_FOUND)
        
        if Booking.objects.filter(user=request.user,event=event).exists():
            return Response({"error":"You have already booked this event"},status=status.HTTP_400_BAD_REQUEST)
        
        if event.available_seats>0:
            Booking.objects.create(user=request.user,event=event)
            event.available_seats -= 1
            event.save()
            
            return Response({"message":"Event booked successfully"},status=status.HTTP_201_CREATED)

class MyBookingsView(APIView):
    def get(self,request):
        bookings =Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        