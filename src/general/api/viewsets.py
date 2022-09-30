import matplotlib.pyplot as plt
from django.apps import apps
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

APPS_NOT_INCLUDE = [
    'django',
    'axes',
    'rest_framework',
    'rest_framework_jwt',
    'admin',
    'auth',
    'authtoken',
    'contenttypes',
    'sessions',
    'blacklist',
]


@api_view(['GET'])
def get_database_info(request: Request) -> HttpResponse:
    fig, ax = plt.subplots()

    labels = []
    counts = []
    for model in apps.get_models(include_auto_created=False):
        _label, _count = (
            model._meta.verbose_name_plural.title(),
            model.objects.all().count(),
        ) if model._meta.app_label not in APPS_NOT_INCLUDE else (None, None)

        if _label or _count:
            labels.append(_label)
            counts.append(_count)

    ax.set_ylim(-1, len(counts) + 0.1)
    ax.set_xlim(0, max(counts) + max(counts))

    bars = ax.barh(range(len(counts)), counts, color='orange')

    ax.bar_label(container=bars, labels=[f'| {counts[i]} | {labels[i]}' for i in range(len(counts))])
    ax.set(xlabel='Количество записей', title='Статистика записей БД')
    ax.set_yticklabels([])
    fig.tight_layout()

    response = HttpResponse(content_type='image/png')
    FigureCanvasAgg(fig).print_png(response)
    return response
