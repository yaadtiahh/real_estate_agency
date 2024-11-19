# Generated by Django 3.2.10 on 2024-11-17 19:36

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20241117_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='user',
        ),
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]