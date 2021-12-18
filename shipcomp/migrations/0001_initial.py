# Generated by Django 4.0 on 2021-12-16 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistributionCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('item_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received', models.BooleanField()),
                ('shipping_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dist_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipcomp.distributioncenter')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=25)),
                ('main_contact', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name=4)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipcomp.item')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipcomp.shipments')),
            ],
        ),
        migrations.AddField(
            model_name='shipments',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipcomp.warehouse'),
        ),
        migrations.AddField(
            model_name='item',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipcomp.vendor'),
        ),
    ]
