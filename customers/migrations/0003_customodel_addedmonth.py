# Generated by Django 3.1.8 on 2021-11-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20211103_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='customodel',
            name='addedmonth',
            field=models.IntegerField(null=True),
        ),
    ]
