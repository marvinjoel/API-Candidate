from django.contrib import admin

from candidates.presidency.models import PresidencyModel, PoliticModel, ExperienceModel, Studies, InvestigationModel


@admin.register(PresidencyModel)
class PresidencyAdmin(admin.ModelAdmin):

    list_display = ['id','name','surname','birthday','photo_cant']

admin.site.register(PoliticModel)
admin.site.register(ExperienceModel)
admin.site.register(Studies)
admin.site.register(InvestigationModel)
