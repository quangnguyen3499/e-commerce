# Generated by Django 4.1 on 2022-08-26 02:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_cartitem_unique_together'),
        ('inventory', '0003_productstock'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('quantity', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=255)),
                ('import_date', models.DateTimeField()),
                ('manufacturer', models.CharField(default='Apple', max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_import', to='store.product')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_import', to='inventory.stock')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
