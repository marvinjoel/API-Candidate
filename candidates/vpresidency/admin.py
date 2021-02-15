from django.contrib import admin

from candidates.vpresidency.models import PVpresidencyModel, SVpresidencyModel


@admin.register(PVpresidencyModel)
class PVpresidencyAdmin(admin.ModelAdmin):
    list_display = ['id','name','surname','photo']


@admin.register(SVpresidencyModel)
class PVpresidencyAdmin(admin.ModelAdmin):
    list_display = ['id','name','surname','photo']