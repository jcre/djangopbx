# Generated by Django 4.0.4 on 2024-01-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provision', '0005_alter_devices_provisioned_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicekeys',
            name='key_type',
            field=models.CharField(max_length=64, verbose_name='Key type'),
        ),
        migrations.AlterField(
            model_name='deviceprofilekeys',
            name='key_type',
            field=models.CharField(max_length=64, verbose_name='Key type'),
        ),
    ]
