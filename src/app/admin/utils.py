from django.urls import reverse


def get_admin_object_hyperlink(model_object):
    """
    function returns a hyperlink to the object in django administration
    """
    try:
        url = reverse(f'admin:{model_object._meta.app_label}_{model_object._meta.model_name}_change', args=[model_object.id])
        return f'<a href="{url}">{model_object}</a>'
    except AttributeError:
        return '-'
