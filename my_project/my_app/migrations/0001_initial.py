# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyFriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_name', models.CharField(max_length=200)),
                ('mobile_no', models.IntegerField()),
            ],
        ),
    ]
