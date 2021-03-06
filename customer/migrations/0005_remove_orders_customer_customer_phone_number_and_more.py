# Generated by Django 4.0.3 on 2022-03-28 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
        ('customer', '0004_alter_customer_station'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='restaurant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='station',
            field=models.IntegerField(default=0),
        ),
    ]
