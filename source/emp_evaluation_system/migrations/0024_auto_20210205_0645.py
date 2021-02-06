# Generated by Django 3.1.3 on 2021-02-05 06:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('emp_evaluation_system', '0023_auto_20210205_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparisongraph',
            name='page',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='emp_evaluation_system.evaluationsystempage'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 6, 45, 9, 410099, tzinfo=utc), help_text='A starting time for the algorithm simulation.'),
        ),
    ]