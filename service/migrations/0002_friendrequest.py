# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 23:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.NullBooleanField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('requestee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestee', to='service.Author')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='service.Author')),
            ],
        ),
    ]
