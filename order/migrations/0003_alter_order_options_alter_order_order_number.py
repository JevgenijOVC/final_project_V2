# Generated by Django 4.2.2 on 2023-07-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=2, max_length=15, unique=True),
            preserve_default=False,
        ),
    ]