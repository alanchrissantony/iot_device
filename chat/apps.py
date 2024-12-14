from django.apps import AppConfig
from .listener import start_socket_listener


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

    def ready(self):
        start_socket_listener()