# Generated by Django 4.0.5 on 2023-02-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chr_models', '0009_remove_company_station_remove_stations_free_bikes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='post_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]