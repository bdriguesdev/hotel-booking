# Generated by Django 3.0.1 on 2020-01-09 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20191209_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.DiscountCoupon'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.RoomPromotion'),
        ),
    ]
