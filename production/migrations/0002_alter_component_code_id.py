# Generated by Django 4.2.2 on 2023-07-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='code_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
