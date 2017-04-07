# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-21 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metarecord', '0019_add_metarecord_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
            options={
                'verbose_name': 'attribute group',
                'verbose_name_plural': 'attribute groups',
            },
        ),
        migrations.AddField(
            model_name='attribute',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='metarecord.AttributeGroup', verbose_name='group'),
        ),
    ]