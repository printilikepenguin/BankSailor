# Generated by Django 4.2.4 on 2023-11-16 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_savingoption_intr_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingoption',
            name='intr_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='savingoption',
            name='intr_rate2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
