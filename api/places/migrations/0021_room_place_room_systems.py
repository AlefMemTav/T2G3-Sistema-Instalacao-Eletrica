# Generated by Django 4.2 on 2024-04-19 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0008_delete_atmosphericdischargesystem'),
        ('places', '0020_remove_room_place_remove_room_systems'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='places.place'),
        ),
        migrations.AddField(
            model_name='room',
            name='systems',
            field=models.ManyToManyField(to='systems.system'),
        ),
    ]
