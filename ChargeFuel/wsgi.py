"""
WSGI config for ChargeFuel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import shutil
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChargeFuel.settings')

if os.environ.get('VERCEL'):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_db = os.path.join(base_dir, 'db.sqlite3')
    dst_db = '/tmp/db.sqlite3'
    if not os.path.exists(dst_db) and os.path.exists(src_db):
        shutil.copy2(src_db, dst_db)

application = get_wsgi_application()

app = application
