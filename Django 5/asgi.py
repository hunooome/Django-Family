import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f'build.settings.{os.getenv("DJANGO_ENV")}')

application = get_asgi_application()
