# Generated by Django 2.2 on 2020-08-16 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work', '0003_auto_20200816_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_goods', models.CharField(max_length=100, verbose_name='товар или услуга')),
                ('goods_text', models.CharField(max_length=2000, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=4, max_digits=8, verbose_name='цена')),
                ('release_date', models.CharField(max_length=100, verbose_name='дата возможной поставки товара клиенту')),
                ('kanban1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Kontakt', verbose_name='наследование конт.')),
            ],
            options={
                'verbose_name': 'Товар - Услуга',
                'verbose_name_plural': 'Товари - Услуги',
            },
        ),
    ]
