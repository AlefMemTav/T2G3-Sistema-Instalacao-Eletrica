# Generated by Django 4.2 on 2024-05-13 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_placeowner_user'),
        ('systems', '0008_delete_atmosphericdischargesystem'),
        ('equipments', '0017_alter_distributionboardequipment_system_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalEquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.placeowner')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.system')),
            ],
            options={
                'db_table': 'equipments_personal_equipment_types',
            },
        ),
    ]
