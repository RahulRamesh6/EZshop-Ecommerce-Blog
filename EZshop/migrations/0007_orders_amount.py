# Generated by Django 5.1.2 on 2024-11-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EZshop', '0006_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]