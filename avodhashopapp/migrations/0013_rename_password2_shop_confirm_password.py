# Generated by Django 3.2.4 on 2021-08-27 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avodhashopapp', '0012_rename_product_item_prodt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='password2',
            new_name='confirm_password',
        ),
    ]