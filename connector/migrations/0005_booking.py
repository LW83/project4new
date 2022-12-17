# Generated by Django 3.2.16 on 2022-12-17 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0004_alter_profile_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_date', models.DateField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('approved', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dog_booking', to='connector.profile')),
                ('rescue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rescue_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]