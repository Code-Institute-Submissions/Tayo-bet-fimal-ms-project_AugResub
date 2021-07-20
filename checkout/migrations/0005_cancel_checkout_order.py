# Generated by Django 3.2.5 on 2021-07-20 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='cancel_checkout_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('cancel_reason', models.TextField(max_length=500)),
                ('return_date', models.DateField(default=django.utils.timezone.now)),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('default_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
