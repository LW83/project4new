# Generated by Django 3.2.16 on 2022-12-27 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['urgency', 'profile_added']},
        ),
    ]