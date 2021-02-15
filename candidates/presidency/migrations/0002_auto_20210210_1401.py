# Generated by Django 3.1.6 on 2021-02-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presidency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=500, verbose_name='Experiencia')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InvestigationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investigation', models.CharField(max_length=500, verbose_name='Investigación')),
            ],
            options={
                'verbose_name': 'Investigation',
                'verbose_name_plural': 'Investigations',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PoliticModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('politc_p', models.CharField(max_length=300, verbose_name='Partido Político')),
            ],
            options={
                'verbose_name': 'Politic',
                'verbose_name_plural': 'Politics',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studes', models.CharField(max_length=500, verbose_name='Estudios')),
            ],
            options={
                'verbose_name': 'Stude',
                'verbose_name_plural': 'Studes',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='presidencymodel',
            options={'ordering': ['id'], 'verbose_name': 'Presiden', 'verbose_name_plural': 'Presidency'},
        ),
    ]