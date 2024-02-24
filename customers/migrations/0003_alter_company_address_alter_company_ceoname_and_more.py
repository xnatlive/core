# Generated by Django 5.0.2 on 2024-02-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ceoName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='tel',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tel',
            field=models.CharField(max_length=12, null=True),
        ),
    ]