# Generated by Django 4.2 on 2024-04-24 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0007_alter_atmosphericdischargeequipment_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='atmosphericdischargeequipment',
            table='equipments_atmospheric_discharge_equipments',
        ),
        migrations.AlterModelTable(
            name='equipmentdetail',
            table='equipments_equipment_details',
        ),
        migrations.AlterModelTable(
            name='equipmenttype',
            table='equipments_equipment_types',
        ),
    ]
