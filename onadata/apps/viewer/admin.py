from reversion.admin import VersionAdmin

from django.contrib import admin

from onadata.apps.viewer.models import (DataDictionary, ParsedInstance, Export)


class DataDictionaryAdmin(VersionAdmin, admin.ModelAdmin):
    exclude = ('user',)

    def get_queryset(self, request):
        qs = super(DataDictionaryAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(DataDictionary, DataDictionaryAdmin)


class ParsedInstanceAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ParsedInstanceAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(ParsedInstance, ParsedInstanceAdmin)


class ExportAdmin(VersionAdmin, admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ExportAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(Export, ExportAdmin)
