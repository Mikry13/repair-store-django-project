from app.conf.environ import env

ALLOWED_HOSTS = ['127.0.0.1']  # host validation is not necessary in 2020
CSRF_TRUSTED_ORIGINS = [
    'https://your.app.origin',
    'http://your.app.origin',
]

if env('DEBUG'):
    ABSOLUTE_HOST = 'http://localhost:3000'
else:
    ABSOLUTE_HOST = 'https://your.app.com'
