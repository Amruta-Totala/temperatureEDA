# Generated by Django 4.0.3 on 2022-05-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0002_alter_product_category_alter_product_num_of_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=100)),
                ('average_temperature', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
