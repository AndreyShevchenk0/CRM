# Generated by Django 2.2 on 2020-08-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20200823_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=8, verbose_name='цена'),
        ),
    ]
