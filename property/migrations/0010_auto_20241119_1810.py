# Generated by Django 3.2.10 on 2024-11-19 15:10

from django.db import migrations


def get_owners(apps, schemaeditor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for owner in Flat.objects.all():
        Owner.objects.get_or_create(
            owner=owner
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(get_owners)
    ]