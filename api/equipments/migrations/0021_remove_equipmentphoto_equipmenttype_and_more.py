# Generated by Django 4.2 on 2024-06-05 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0020_remove_equipmentphoto_equipment_detail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentphoto',
            name='equipmentType',
        ),
        migrations.RemoveField(
            model_name='equipmentphoto',
            name='personalEquipmentType',
        ),
        migrations.AddField(
            model_name='equipmentdetail',
            name='personalEquipmentType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equipments.personalequipmenttype'),
        ),
        migrations.AlterField(
            model_name='equipmentdetail',
            name='equipmentType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equipments.equipmenttype'),
        ),
    ]
