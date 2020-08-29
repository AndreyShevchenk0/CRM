# Generated by Django 2.2 on 2020-08-16 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='kanban',
            field=models.ForeignKey(choices=[('ПЗ', 'Первий звонок'), ('ДК', 'Договор'), ('$', 'Проплата услуги == товара'), ('ПТ', 'Получение товара')], on_delete=django.db.models.deletion.CASCADE, to='work.Kontakt'),
        ),
    ]
