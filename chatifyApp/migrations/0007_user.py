# Generated by Django 5.0.2 on 2024-03-11 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatifyApp', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('coins', models.IntegerField(default=100)),
                ('theme_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatifyApp.themes')),
            ],
        ),
    ]
