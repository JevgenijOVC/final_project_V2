# Generated by Django 4.2.2 on 2023-07-19 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_id_alter_product_code_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_drw_number']},
        ),
    ]
