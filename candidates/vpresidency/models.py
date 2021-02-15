from django.db import models


class PVpresidencyModel(models.Model):

    def Pcant_url(self, filename):
        ruta = f'static/candidate/vpresidency/first/{self.name}/{filename}'
        return ruta

    name = models.CharField(verbose_name='Nombre', max_length=100)
    surname = models.CharField(verbose_name='Apellido', max_length=100)
    photo = models.ImageField(upload_to=Pcant_url, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='PVpresiden'
        verbose_name_plural='PVpresidency'
        ordering = ['id']


class SVpresidencyModel(models.Model):

    def Scant_url(self, filename):
        ruta = f'static/candidate/vpresidency/second/{self.name}/{filename}'
        return ruta

    name = models.CharField(verbose_name='Nombre', max_length=100)
    surname = models.CharField(verbose_name='Apellido', max_length=100)
    photo = models.ImageField(upload_to=Scant_url, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='SVpresiden'
        verbose_name_plural='SVpresidency'
        ordering = ['id']