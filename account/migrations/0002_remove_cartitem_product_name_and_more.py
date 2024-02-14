# Generated by Django 4.2.2 on 2023-09-27 07:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product_price',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product_quantity',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='added_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customerregistration',
            name='Is_Approved',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.PositiveIntegerField(default=0)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.vendorartwork')),
            ],
        ),
    ]
