from rest_framework import serializers

from cam.models import Events, Cam, Event_type


class CameraSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255, source='id_cam')
    external_id = serializers.CharField(max_length=255)
    class Meta:
        model = Cam
        fields = ['id_cam', 'external_id']


class EventsSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=100)
    event_type = serializers.CharField(max_length=100)
    camera = CameraSerializer()
    image_uri = serializers.URLField()
    class Meta:
        model = Events
        fields = ['type', 'event_type', 'camera', 'image_uri']
        read_only_fields = []

    def create(self, validated_data):
        print(validated_data)
        return Events.objects.create(**validated_data)