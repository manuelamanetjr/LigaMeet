# Generated by Django 5.0.1 on 2024-10-08 04:12

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SPORT_NAME', models.CharField(max_length=100)),
                ('SPORT_RULES_AND_REGULATIONS', models.TextField()),
                ('EDITED_AT', models.DateTimeField(default=django.utils.timezone.now)),
                ('IMAGE', models.ImageField(blank=True, null=True, upload_to='sports_icon/')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FILE_PATH', models.FileField(upload_to='files/')),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EVENT_NAME', models.CharField(max_length=100)),
                ('EVENT_DATE_START', models.DateTimeField()),
                ('EVENT_DATE_END', models.DateTimeField()),
                ('EVENT_LOCATION', models.CharField(max_length=255)),
                ('EVENT_STATUS', models.CharField(choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='upcoming', max_length=10)),
                ('EVENT_ORGANIZER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to=settings.AUTH_USER_MODEL)),
                ('SPORT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='ligameet.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SUB_PLAN', models.CharField(max_length=50)),
                ('SUB_DATE_STARTED', models.DateTimeField(default=django.utils.timezone.now)),
                ('SUB_DATE_END', models.DateTimeField()),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEAM_NAME', models.CharField(max_length=100)),
                ('TEAM_TYPE', models.CharField(max_length=50)),
                ('COACH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('SPORT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MATCH_TYPE', models.CharField(max_length=50)),
                ('MATCH_CATEGORY', models.CharField(max_length=50)),
                ('MATCH_SCORE', models.IntegerField(default=0)),
                ('MATCH_DATE', models.DateTimeField()),
                ('MATCH_STATUS', models.CharField(max_length=20)),
                ('TEAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.team')),
            ],
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATUS', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('REQUEST_DATE', models.DateTimeField(default=django.utils.timezone.now)),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('TEAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EVENT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.event')),
                ('TEAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IS_WINNER', models.BooleanField(default=False)),
                ('MATCH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.match')),
                ('TEAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IS_CAPTAIN', models.BooleanField(default=False)),
                ('TEAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.team')),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamRegistrationFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REGISTRATION_FEE', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('IS_PAID', models.BooleanField(default=False)),
                ('MATCH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.match')),
                ('TEAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.team')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PAYMENT_AMOUNT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PAYMENT_DATE', models.DateTimeField(default=django.utils.timezone.now)),
                ('SUBSCRIPTION_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ligameet.subscription')),
                ('TEAM_REGISTRATION_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ligameet.teamregistrationfee')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TRANSACTION_DATE', models.DateTimeField(default=django.utils.timezone.now)),
                ('TRANSACTION_AMOUNT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PAYMENT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.payment')),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IS_WINNER', models.BooleanField(default=False)),
                ('MATCH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.match')),
                ('TEAM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.team')),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistrationFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IS_PAID', models.BooleanField(default=False)),
                ('USER_MATCH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.usermatch')),
            ],
        ),
        migrations.CreateModel(
            name='VolleyballStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VB_STATS_PT_COUNT', models.IntegerField(default=0)),
                ('VB_STATS_ASSIST', models.IntegerField(default=0)),
                ('VB_STATS_BLOCK', models.IntegerField(default=0)),
                ('VB_STATS_ERROR', models.IntegerField(default=0)),
                ('VB_STATS_IS_MVP', models.BooleanField(default=False)),
                ('VB_STATS_SET', models.IntegerField(default=0)),
                ('MATCH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.match')),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('USER_MATCH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.usermatch')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WALLET_BALANCE', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='WALLET_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.wallet'),
        ),
        migrations.CreateModel(
            name='SportsEvent',
            fields=[
                ('EVENT_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ligameet.event')),
                ('SPORTS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligameet.sport')),
            ],
        ),
        migrations.AddConstraint(
            model_name='joinrequest',
            constraint=models.UniqueConstraint(fields=('USER_ID', 'TEAM_ID'), name='unique_join_request'),
        ),
        migrations.AddConstraint(
            model_name='teamevent',
            constraint=models.UniqueConstraint(fields=('TEAM_ID', 'EVENT_ID'), name='unique_team_event'),
        ),
        migrations.AddConstraint(
            model_name='teammatch',
            constraint=models.UniqueConstraint(fields=('TEAM_ID', 'MATCH_ID'), name='unique_team_match'),
        ),
        migrations.AddConstraint(
            model_name='teamparticipant',
            constraint=models.UniqueConstraint(fields=('USER_ID', 'TEAM_ID'), name='unique_team_user'),
        ),
        migrations.AddConstraint(
            model_name='usermatch',
            constraint=models.UniqueConstraint(fields=('MATCH_ID', 'USER_ID'), name='unique_user_match'),
        ),
    ]
