# Generated by Django 3.1.6 on 2021-10-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrm', '0003_recordgroup_field_definitions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordgroup',
            name='field_definitions',
            field=models.JSONField(default=dict),
        ),
    ]
