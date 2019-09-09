# If you are using development settings, remember to set os.environ.setdefault("DJANGO_SETTINGS_MODULE", "votelly.settings.development")
# instead of just votelly.settings

from .common import *

DEBUG = True

STATIC_URL = '/static/'
MEDIA_URL = '/pics/'
MEDIA_ROOT = BASE_DIR