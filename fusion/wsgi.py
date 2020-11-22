"""
WSGI config for fusion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling # o Cling serve para apresentar arquivos estaticos como css, java, bootstrap etc, e o mediacling para apresentar os arquivos que os usuarios fizeram upload para o sistema

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')

application = Cling(MediaCling(get_wsgi_application()))
