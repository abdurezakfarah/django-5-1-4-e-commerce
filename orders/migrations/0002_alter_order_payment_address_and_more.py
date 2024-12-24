# Generated by Django 5.1.4 on 2024-12-23 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='payments', to='users.address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='shipments', to='users.address'),
        ),
    ]