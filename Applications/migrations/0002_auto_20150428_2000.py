# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareToApplicant',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechToApplicant',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='applicationStatus',
            field=models.CharField(max_length=1, choices=[('r', 'Received'), ('v', 'Reviewed'), ('a', 'Accepted'), ('w', 'Wait list'), ('d', 'Declined'), ('f', 'Flagged for Abuse')], default='r'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='dietaryRestrictions',
            field=models.CharField(max_length=1, choices=[('n', 'None'), ('v', 'Vegetarian'), ('g', 'Vegan'), ('k', 'Kosher'), ('h', 'Halal'), ('o', 'Other')], default='n'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='linkedIn',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^(http(?:s)?\\:\\/\\/[a-zA-Z0-9]+(?:(?:\\.|\\-)[a-zA-Z0-9]+)+(?:\\:\\d+)?(?:\\/[\\w\\-]+)*(?:\\/?|\\/\\w+\\.[a-zA-Z]{2,4}(?:\\?[\\w]+\\=[\\w\\-]+)?)?(?:\\&[\\w]+\\=[\\w\\-]+)*)$', message='Not a proper website url')], max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='needReimbursement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicant',
            name='otherDietaryRestrictions',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='specialAccommodations',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='travelMethod',
            field=models.CharField(max_length=1, choices=[('p', 'plane'), ('t', 'train'), ('c', 'car')], default='c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='travelingFrom',
            field=models.TextField(default='East Lansing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertype',
            name='deviceKey',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usertype',
            name='genderIdentity',
            field=models.CharField(max_length=2, choices=[('m', 'Male'), ('f', 'Female'), ('na', 'Prefer Not to Disclose')], default='na'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='website',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^(http(?:s)?\\:\\/\\/[a-zA-Z0-9]+(?:(?:\\.|\\-)[a-zA-Z0-9]+)+(?:\\:\\d+)?(?:\\/[\\w\\-]+)*(?:\\/?|\\/\\w+\\.[a-zA-Z]{2,4}(?:\\?[\\w]+\\=[\\w\\-]+)?)?(?:\\&[\\w]+\\=[\\w\\-]+)*)$', message='Not a proper website url')], max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='techtoapplicant',
            name='applicant',
            field=models.ForeignKey(to='Applications.Applicant'),
        ),
        migrations.AddField(
            model_name='techtoapplicant',
            name='tech',
            field=models.ForeignKey(to='Applications.Tech'),
        ),
        migrations.AddField(
            model_name='hardwaretoapplicant',
            name='applicant',
            field=models.ForeignKey(to='Applications.Applicant'),
        ),
        migrations.AddField(
            model_name='hardwaretoapplicant',
            name='hardware',
            field=models.ForeignKey(to='Applications.Hardware'),
        ),
    ]
