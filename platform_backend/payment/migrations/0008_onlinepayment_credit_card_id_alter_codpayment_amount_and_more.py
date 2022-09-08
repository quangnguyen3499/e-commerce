# Generated by Django 4.0.6 on 2022-09-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_rename_total_order_invoice_total_remain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codpayment',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_charges',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_due',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_remain',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='onlinepayment',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
