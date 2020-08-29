# Generated by Django 2.2 on 2020-08-16 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('deal', '0004_auto_20200816_2102'),
        ('work', '0003_auto_20200816_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='Состояние товара')),
                ('view1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Kontakt', verbose_name='Покупатель + Товар')),
                ('view2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deal.deal', verbose_name='Статус сделки')),
            ],
            options={
                'verbose_name': 'Воронка',
                'verbose_name_plural': 'Воронки',
            },
        ),
    ]