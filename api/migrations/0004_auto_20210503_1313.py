# Generated by Django 3.1.6 on 2021-05-03 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210503_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submissions',
            old_name='date_Created',
            new_name='date_created',
        ),
    ]
