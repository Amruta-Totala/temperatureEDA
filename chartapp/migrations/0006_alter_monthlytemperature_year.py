# Generated by Django 4.0.3 on 2022-06-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0005_alter_monthlytemperature_apr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlytemperature',
            name='year',
            field=models.IntegerField(max_length=100),
        ),
    ]
