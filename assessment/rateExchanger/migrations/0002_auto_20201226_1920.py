# Generated by Django 3.1.4 on 2020-12-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateExchanger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='rate',
            field=models.DecimalField(decimal_places=6, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='from_currency',
            field=models.CharField(default='EUR', max_length=10),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='to_currency',
            field=models.CharField(max_length=10, null=True),
        ),
    ]