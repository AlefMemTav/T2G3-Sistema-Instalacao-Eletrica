# Generated by Django 4.2 on 2024-04-11 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_placeowner_user'),
        ('places', '0010_alter_place_place_owner_alter_room_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.placeowner'),
        ),
    ]
