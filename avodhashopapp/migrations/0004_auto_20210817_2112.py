# Generated by Django 3.2.4 on 2021-08-17 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avodhashopapp', '0003_auto_20210817_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='confirmpassword',
            new_name='confirm_password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
