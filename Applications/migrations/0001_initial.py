# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('General', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('DoB', models.DateField()),
                ('year', models.CharField(choices=[('FR', 'Freshman'), ('SP', 'Sophomore'), ('JR', 'Junior'), ('SN', 'Senior'), ('HS', 'High School'), ('GD', 'Graduate'), ('OT', 'Other')], max_length=2)),
                ('major', models.CharField(max_length=100)),
                ('github', models.CharField(null=True, blank=True, max_length=100)),
                ('website', models.CharField(null=True, blank=True, max_length=100)),
                ('resume', models.FileField(null=True, blank=True, upload_to='')),
                ('otherHackathons', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HackathonToApplicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('applicant', models.ForeignKey(to='Applications.Applicant')),
                ('hackathon', models.ForeignKey(to='Applications.Hackathon')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolAbbreviations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('abbr', models.CharField(max_length=50)),
                ('school', models.ForeignKey(to='Applications.School')),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TechToMentor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('position', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('wantsToMentor', models.BooleanField(default=False)),
                ('phoneNumber', models.CharField(unique=True, blank=True, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userAffiliation', models.ForeignKey(blank=True, to='General.Sponsor', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='techtomentor',
            name='mentor',
            field=models.ForeignKey(to='Applications.UserType'),
        ),
        migrations.AddField(
            model_name='techtomentor',
            name='tech',
            field=models.ForeignKey(to='Applications.Tech'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='school',
            field=models.ForeignKey(to='Applications.School'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='user',
            field=models.OneToOneField(to='Applications.UserType'),
        ),
    ]
