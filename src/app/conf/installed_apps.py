APPS = [
    # Default models, env, settings etc.
    'app',

    # Token etc. config app.
    'a12n',

    # User etc. config app.
    'users',
]

MODEL_APPS = [
    'stock_items.apps.StockItemsConfig',
    'stock_orders.apps.StockOrdersConfig',
    'sales.apps.SalesConfig',
    'logs.apps.LogsConfig',
]

THIRD_PARTY_APPS = [
    # OpenApi Swagger
    'drf_spectacular',
    'drf_spectacular_sidecar',

    # For API
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_jwt.blacklist',
    'django_filters',

    # Access Logs
    'axes',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = APPS + MODEL_APPS + THIRD_PARTY_APPS
