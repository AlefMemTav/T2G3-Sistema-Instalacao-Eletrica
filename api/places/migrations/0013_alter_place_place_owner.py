# Generated by Django 4.2 on 2024-04-11 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_placeowner_user'),
        ('places', '0012_alter_place_place_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.placeowner'),
        ),
    ]
