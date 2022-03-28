# Generated by Django 4.0.3 on 2022-03-27 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_remove_train_stations_train_stations'),
        ('customer', '0003_customer_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.station'),
        ),
    ]