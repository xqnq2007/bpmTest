"""
WSGI config for bpmTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/Users/wangziqiang/djangoprojects/bpmTest')
sys.path.append('/Users/wangziqiang/djangoprojects/bpmTest/bpmTest')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bpmTest.settings")

application = get_wsgi_application()
