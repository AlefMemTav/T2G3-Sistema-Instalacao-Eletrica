# Generated by Django 4.2 on 2024-05-03 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0008_delete_atmosphericdischargesystem'),
        ('equipments', '0012_sructeredcablingequipment_iluminationequipment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='atmosphericdischargeequipment',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
        migrations.AddField(
            model_name='distributionboardequipment',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
        migrations.AddField(
            model_name='electricalcircuitequipment',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
        migrations.AddField(
            model_name='electricallineequipment',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
        migrations.AddField(
            model_name='electricalloadequipment',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
        migrations.AddField(
            model_name='firealarmequipment',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
        migrations.AddField(
            model_name='iluminationequipment',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
        migrations.AddField(
            model_name='sructeredcablingequipment',
            name='system',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.system'),
        ),
    ]
