# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0004_auto_20150529_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='dribble',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
    ]
