# Generated by Django 4.2 on 2024-04-18 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_placeowner_user'),
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='placeOwner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.placeowner'),
        ),
        migrations.DeleteModel(
            name='AtmosphericDischargeSystem',
        ),
    ]
