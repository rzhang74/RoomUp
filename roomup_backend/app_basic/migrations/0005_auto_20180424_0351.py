# Generated by Django 2.0.2 on 2018-04-24 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_basic', '0004_auto_20180423_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advanceduser',
            name='major',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
