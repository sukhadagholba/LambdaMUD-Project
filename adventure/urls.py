from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('whisper', api.whisper),
    url('shout', api.shout),
    url('playersall', api.playersall),
]
