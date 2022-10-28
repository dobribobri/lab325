# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1068039/data/www/lab325.dobrix.ru/lab325')
sys.path.insert(1, '/var/www/u1068039/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'lab325.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
