# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.FileField(upload_to='')),
                ('link', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=2, choices=[('b', 'Bronze'), ('s', 'Silver'), ('g', 'Gold'), ('p', 'Platnuim')], default='b')),
                ('type', models.CharField(max_length=2, choices=[('s', 'Startup'), ('c', 'Corporate')], default='s')),
            ],
        ),
    ]
