from django.urls import path

from cam.views import CamView

urlpatterns = [
    path('test/', CamView.as_view(), name='test'),
]
