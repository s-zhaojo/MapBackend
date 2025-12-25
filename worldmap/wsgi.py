# wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "worldmap.settings")  # <- keep this if worldmap/settings.py exists
application = get_wsgi_application()
