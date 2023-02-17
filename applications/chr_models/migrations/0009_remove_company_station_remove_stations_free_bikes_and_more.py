# Generated by Django 4.0.5 on 2023-02-17 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chr_models', '0008_alter_stations_ebikes_alter_stations_has_ebikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='station',
        ),
        migrations.RemoveField(
            model_name='stations',
            name='free_bikes',
        ),
        migrations.RemoveField(
            model_name='stations',
            name='payment_terminal',
        ),
        migrations.AddField(
            model_name='stations',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chr_models.company'),
        ),
        migrations.AddField(
            model_name='stations',
            name='empty_slots',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='exist',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='id_bike',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='post_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='renting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='returning',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='time_stamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='uid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='FreeBikes',
        ),
        migrations.DeleteModel(
            name='PaymentTerminal',
        ),
    ]