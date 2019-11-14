from channels.routing import ProtocolTypeRouter
from django.conf.urls import url
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from levels.consumer import CTFConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        [
            path('flag', CTFConsumer),
        ]
    )
})