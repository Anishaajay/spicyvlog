# Generated by Django 3.2.4 on 2021-08-17 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avodhashopapp', '0002_auto_20210817_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='password1',
            new_name='confirmpassword',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='password2',
            new_name='password',
        ),
    ]
