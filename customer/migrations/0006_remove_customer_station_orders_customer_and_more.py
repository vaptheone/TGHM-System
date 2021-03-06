# Generated by Django 4.0.3 on 2022-03-28 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_orders_customer_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='station',
        ),
        migrations.AddField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
