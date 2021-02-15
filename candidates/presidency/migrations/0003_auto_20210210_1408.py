# Generated by Django 3.1.6 on 2021-02-10 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presidency', '0002_auto_20210210_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='presidencymodel',
            name='experience',
            field=models.ManyToManyField(blank=True, to='presidency.ExperienceModel'),
        ),
        migrations.AddField(
            model_name='presidencymodel',
            name='investigation',
            field=models.ManyToManyField(blank=True, to='presidency.InvestigationModel'),
        ),
        migrations.AddField(
            model_name='presidencymodel',
            name='politic_part',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='presidency.politicmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presidencymodel',
            name='studes',
            field=models.ManyToManyField(blank=True, to='presidency.Studies'),
        ),
    ]