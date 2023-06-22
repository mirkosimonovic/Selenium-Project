"""
WSGI config for pruebapractica project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
import django
django.setup()
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pruebapractica.settings')
import django
django.setup()
from django.core.wsgi import get_wsgi_application


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
application = get_wsgi_application()
