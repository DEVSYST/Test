# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medfreq', '0004_auto_20161202_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illnessitem',
            name='duty_cycle',
            field=models.IntegerField(null=True),
        ),
    ]
