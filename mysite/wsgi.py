"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
settings_path = '/home/JaCait/jacait.pythonanywhere.com'
sys.path.insert(0, settings_path)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Set the 'application' variable to the Django wsgi app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

