# Generated by Django 4.1.5 on 2023-02-23 23:03

import creditcards.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_checkout_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cardnumber',
            field=creditcards.models.CardNumberField(max_length=16, verbose_name='Card Number'),
        ),
    ]
