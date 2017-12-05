# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-05 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ORMAuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('refresh_token', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.ORMPerson')),
            ],
            options={
                'verbose_name': 'Auth token',
                'verbose_name_plural': 'Auth tokens',
            },
        ),
    ]