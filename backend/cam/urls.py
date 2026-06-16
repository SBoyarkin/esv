from django.urls import path

from cam.views import CamView, EventsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', EventsView, basename='events')

urlpatterns = [
    path('test/', CamView.as_view(), name='test'),

]

urlpatterns += router.urls