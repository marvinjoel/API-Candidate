# Generated by Django 3.1.6 on 2021-02-10 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpresidency', '0001_initial'),
        ('presidency', '0003_auto_20210210_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='presidencymodel',
            name='pvpresidency',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='vpresidency.pvpresidencymodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presidencymodel',
            name='svpresidency',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='vpresidency.svpresidencymodel'),
            preserve_default=False,
        ),
    ]