# Generated by Django 5.0.7 on 2024-09-16 17:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRST_NAME', models.CharField(default='', max_length=30)),
                ('LAST_NAME', models.CharField(default='', max_length=30)),
                ('MIDDLE_NAME', models.CharField(blank=True, max_length=30, null=True)),
                ('DATE_OF_BIRTH', models.DateField(blank=True, null=True)),
                ('GENDER', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='-', max_length=1)),
                ('ADDRESS', models.CharField(blank=True, max_length=255, null=True)),
                ('HEIGHT', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('WEIGHT', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('PHONE', models.CharField(blank=True, max_length=15, null=True)),
                ('INV_CODE', models.CharField(blank=True, max_length=50, null=True)),
                ('IS_COACH', models.BooleanField(default=False)),
                ('IS_ATHLETE', models.BooleanField(default=False)),
                ('IS_SCOUT', models.BooleanField(default=False)),
                ('IS_EVENT_ORG', models.BooleanField(default=False)),
                ('image', models.ImageField(default='user_default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
