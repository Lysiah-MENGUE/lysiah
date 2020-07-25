from .settings import *

DEBUG = False
TEMPLATE_DEBUG = True


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS =['cv-mengue.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
