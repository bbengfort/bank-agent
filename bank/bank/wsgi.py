"""
WSGI config for bank project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application

# load .env file
dotenv.load_dotenv(dotenv.find_dotenv())

# set default environment variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank.settings")

# export the wsgi application for import
application = get_wsgi_application()
