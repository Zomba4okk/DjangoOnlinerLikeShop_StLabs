# Generated by Django 3.1.7 on 2021-03-21 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210321_1825'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart_Product_m2m',
            new_name='CartProductM2M',
        ),
        migrations.RenameModel(
            old_name='Order_Product_m2m',
            new_name='OrderProductM2M',
        ),
    ]