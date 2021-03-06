# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xbaIP')),
                ('open_port', models.CharField(max_length=1000, verbose_name=b'\xe5\xbc\x80\xe6\x94\xbe\xe7\xab\xaf\xe5\x8f\xa3')),
                ('status', models.IntegerField(choices=[(1, b'\xe7\xa9\xba\xe9\x97\xb2'), (2, b'\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad'), (3, b'\xe6\x8a\xa5\xe5\xba\x9f')], verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\x8a\xb6\xe6\x80\x81')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name_plural': '\u4e3b\u673a',
            },
        ),
    ]
