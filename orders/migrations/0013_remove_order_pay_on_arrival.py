# Generated by Django 2.2.11 on 2020-05-11 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pay_on_arrival',
        ),
    ]
