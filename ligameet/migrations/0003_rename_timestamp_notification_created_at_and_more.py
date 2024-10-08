# Generated by Django 5.0.1 on 2024-10-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0002_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
