# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0002_auto_20150428_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='freeResponce',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
