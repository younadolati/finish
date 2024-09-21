import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from accounts.routing import websocket_urlpatterns

application=get_asgi_application()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finish.settings')

application=ProtocolTypeRouter(
    {
        'http':get_asgi_application(),
        'websocket':AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
                
        )

    }
)
