# Generated by Django 4.2 on 2024-04-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0001_initial'),
        ('places', '0005_alter_room_floor_alter_room_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='systems',
            field=models.ManyToManyField(to='systems.system'),
        ),
    ]
