# Generated by Django 4.2 on 2024-04-25 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0010_rename_type_equipmenttype_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipmentdetail',
            old_name='placeOwner',
            new_name='place_owner',
        ),
    ]
