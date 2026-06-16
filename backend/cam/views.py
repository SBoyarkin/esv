from asyncio import Event

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics

from cam.models import Events, Event_type, Cam

from cam.serializers import EventsSerializer


# Create your views here.


class CamView(APIView):
    def post(self, request):
        return Response('test')


class EventsView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def perform_create(self, serializer):

        event = serializer.validated_data['event_type']
        event_type, _ = Event_type.objects.get_or_create(event_type=event)



        id_cam = serializer.validated_data['camera']['id_cam']
        external_id = serializer.validated_data['camera']['external_id']
        cam, _ = Cam.objects.get_or_create(id_cam=id_cam, external_id=external_id)
        serializer.save(event_type=event_type, camera=cam)
