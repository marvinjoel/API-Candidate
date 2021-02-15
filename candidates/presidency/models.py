from datetime import datetime

from django.db import models
from django.utils.safestring import mark_safe

from candidates.vpresidency.models import PVpresidencyModel, SVpresidencyModel


class PoliticModel(models.Model):
    politc_p = models.CharField(verbose_name='Partido Político', max_length=300)
    def __str__(self):
        return self.politc_p

    class Meta:
        verbose_name='Politic'
        verbose_name_plural= 'Politics'
        ordering = ['id']


class ExperienceModel(models.Model):
    experience = models.CharField(verbose_name='Experiencia', max_length=500)
    def __str__(self):
        return self.experience

    class Meta:
        verbose_name='Experience'
        verbose_name_plural= 'Experiences'
        ordering = ['id']


class Studies(models.Model):
    studes = models.CharField(verbose_name='Estudios', max_length=500)

    def __str__(self):
        return self.studes

    class Meta:
        verbose_name='Stude'
        verbose_name_plural= 'Studes'
        ordering = ['id']

class InvestigationModel(models.Model):
    investigation = models.CharField(verbose_name='Investigación', max_length=500)

    def __str__(self):
        return self.investigation

    class Meta:
        verbose_name='Investigation'
        verbose_name_plural= 'Investigations'
        ordering = ['id']



class PresidencyModel(models.Model):

    def pres_url(self, filename):
        ruta = f'static/candidate/presidency/{self.name}/{filename}'
        return ruta

    def photo_cant(self):
        return mark_safe(f'<img src="{self.photo}" width=50px height=50px />')

    name = models.CharField(verbose_name='Nombre', max_length=150)
    surname = models.CharField(verbose_name='Apellido', max_length=150)
    birthday = models.DateField(verbose_name='Fecha de Nacimiento', default=datetime.now)
    photo = models.ImageField(upload_to=pres_url, blank=True, null=True, verbose_name='Foto')

    politic_part = models.OneToOneField(PoliticModel, on_delete=models.CASCADE, blank=True)
    experience = models.ManyToManyField(ExperienceModel, blank=True)
    studes = models.ManyToManyField(Studies, blank=True)
    investigation = models.ManyToManyField(InvestigationModel, blank=True)
    #VICE presidencia
    pvpresidency = models.OneToOneField(PVpresidencyModel, on_delete=models.CASCADE, blank=True)
    svpresidency = models.OneToOneField(SVpresidencyModel, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Presiden'
        verbose_name_plural='Presidency'
        ordering = ['id']
