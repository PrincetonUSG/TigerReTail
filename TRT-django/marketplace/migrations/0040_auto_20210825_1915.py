# Generated by Django 3.1.8 on 2021-08-26 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0039_auto_20210825_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='emailActivity',
            new_name='email_activity',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='emailUnreadNotification',
            new_name='email_unread_notification',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='remindSetEmailSettings',
            new_name='remind_set_email_settings',
        ),
    ]
