# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('created', models.DateTimeField(verbose_name=b'date created')),
                ('updated', models.DateTimeField(verbose_name=b'date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('created', models.DateTimeField(verbose_name=b'date created')),
                ('updated', models.DateTimeField(verbose_name=b'date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(to='wsmanager.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Slope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=6)),
                ('opened', models.BooleanField()),
                ('kms', models.FloatField()),
                ('created', models.DateTimeField(verbose_name=b'date created')),
                ('updated', models.DateTimeField(verbose_name=b'date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('created', models.DateTimeField(verbose_name=b'date created')),
                ('updated', models.DateTimeField(verbose_name=b'date updated')),
                ('country', models.ForeignKey(to='wsmanager.Country')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('passwd', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(verbose_name=b'date created')),
                ('updated', models.DateTimeField(verbose_name=b'date updated')),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='user',
            field=models.ForeignKey(to='wsmanager.User'),
        ),
        migrations.AddField(
            model_name='slope',
            name='station',
            field=models.ForeignKey(to='wsmanager.Station'),
        ),
        migrations.AddField(
            model_name='price',
            name='station',
            field=models.ForeignKey(to='wsmanager.Station'),
        ),
        migrations.AddField(
            model_name='parking',
            name='station',
            field=models.ForeignKey(to='wsmanager.Station'),
        ),
    ]
