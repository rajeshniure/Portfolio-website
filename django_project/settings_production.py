from .settings import *

# Production settings
DEBUG = False

# Security settings
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Remove django-compressor if it's causing issues in production
if 'compressor' in INSTALLED_APPS:
    INSTALLED_APPS.remove('compressor')
    
if 'compressor.finders.CompressorFinder' in STATICFILES_FINDERS:
    STATICFILES_FINDERS.remove('compressor.finders.CompressorFinder')

# Disable django-compressor
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False 