# Generated by Django 3.2.7 on 2021-10-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0004_auto_20211023_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
