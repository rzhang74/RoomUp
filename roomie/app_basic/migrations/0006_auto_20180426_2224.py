# Generated by Django 2.0.2 on 2018-04-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_basic', '0005_auto_20180424_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=30),
        ),
    ]