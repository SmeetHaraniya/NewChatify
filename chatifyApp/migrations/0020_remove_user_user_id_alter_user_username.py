# Generated by Django 5.0.2 on 2024-03-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatifyApp', '0019_alter_chats_msg_date_alter_chats_msg_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
