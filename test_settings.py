SECRET_KEY = "123456"
NEVERCACHE_KEY = SECRET_KEY + "12345"

INSTALLED_APPS = (
    "mezzanine_rest",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'PAGINATE_BY': 10
}
