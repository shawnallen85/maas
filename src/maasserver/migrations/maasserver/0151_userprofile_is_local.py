# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-22 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("maasserver", "0150_add_pod_commit_ratios")]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="is_local",
            field=models.BooleanField(default=True),
        )
    ]
