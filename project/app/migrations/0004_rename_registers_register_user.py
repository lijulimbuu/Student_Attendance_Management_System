# Generated by Django 4.2.3 on 2024-04-04 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_register_registers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registers',
            new_name='Register_User',
        ),
    ]
