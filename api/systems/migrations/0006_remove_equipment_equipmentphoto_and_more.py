# Generated by Django 4.2 on 2024-04-18 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0005_alter_equipment_equipmentphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='equipmentPhoto',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='equipmentType',
        ),
        migrations.RemoveField(
            model_name='equipmenttype',
            name='system',
        ),
        migrations.DeleteModel(
            name='AtmosphericDischargeSystem',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='EquipmentPhoto',
        ),
        migrations.DeleteModel(
            name='EquipmentType',
        ),
    ]