# Generated by Django 4.2 on 2024-05-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0026_alter_area_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='floor',
            field=models.IntegerField(default=0),
        ),
    ]
