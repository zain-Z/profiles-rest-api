# Generated by Django 3.1.3 on 2020-12-05 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='user_profile',
            new_name='userf_profile',
        ),
    ]
