# Generated by Django 4.0 on 2021-12-21 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0004_payment_refund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ticketing.seasonticket'),
        ),
    ]
