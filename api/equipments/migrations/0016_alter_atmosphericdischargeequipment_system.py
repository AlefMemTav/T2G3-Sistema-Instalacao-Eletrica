# Generated by Django 4.2 on 2024-05-03 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0008_delete_atmosphericdischargesystem'),
        ('equipments', '0015_rename_sructeredcablingequipment_structuredcablingequipment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmosphericdischargeequipment',
            name='system',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
    ]
