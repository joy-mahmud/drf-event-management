from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework import status

class EventListView(APIView):
    def get(self,request):
        events = Event.objects.all()
        print(events)
        serializer = EventSerializer(events,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)