# Generated by Django 5.0.2 on 2024-03-11 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatifyApp', '0009_rename_fname_user_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='latsname',
            new_name='lastname',
        ),
    ]
