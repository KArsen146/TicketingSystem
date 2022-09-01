# Generated by Django 4.0 on 2021-12-21 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_remove_manager_user_ptr_alter_seasonticket_seat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sector',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('sector', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='sector',
            unique_together={('stadium', 'number')},
        ),
    ]