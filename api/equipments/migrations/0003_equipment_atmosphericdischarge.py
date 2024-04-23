# Generated by Django 4.2 on 2024-04-23 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atmosphericdischarges', '0003_remove_atmosphericdischarge_equipment'),
        ('equipments', '0002_equipment_placeowner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='atmosphericDischarge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atmosphericdischarges.atmosphericdischarge'),
        ),
    ]