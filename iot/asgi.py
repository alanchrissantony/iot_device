import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/data/", consumers.DataConsumer.as_asgi()),
        ])
    ),
})


