# Generated by Django 4.0 on 2021-12-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0006_refundingpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='refundingpayment',
            name='pay_from',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refundingpayment',
            name='pay_to',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refundingpayment',
            name='value',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
            preserve_default=False,
        ),
    ]
