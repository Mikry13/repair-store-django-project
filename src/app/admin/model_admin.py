from django.contrib import admin


class DefaultModelAdmin(admin.ModelAdmin):
    list_exclude = ()

    def __init__(self, model, admin_site):
        if self.list_display == ('__str__',):
            self.list_display = [field.name for field in model._meta.fields if field.name not in self.list_exclude]
        super(DefaultModelAdmin, self).__init__(model, admin_site)
