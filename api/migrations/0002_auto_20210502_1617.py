# Generated by Django 3.1.6 on 2021-05-02 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submissions',
            old_name='First_Name',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='submissions',
            old_name='Last_Name',
            new_name='LastName',
        ),
    ]