# Generated by Django 4.1.5 on 2023-01-27 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_vendor_orderitems_deliveryorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='item_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]