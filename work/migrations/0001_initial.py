# Generated by Django 2.2 on 2020-08-15 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='фамилия')),
                ('midl_name', models.CharField(max_length=20, verbose_name='Очество')),
                ('companiName', models.CharField(max_length=40, verbose_name='имя компании')),
                ('logo', models.ImageField(upload_to='', verbose_name='лого')),
                ('age', models.CharField(max_length=2, verbose_name='возраст')),
                ('pasport', models.CharField(max_length=200, verbose_name='серия паспорта')),
                ('INN', models.CharField(max_length=20, verbose_name='инн')),
                ('r_r', models.CharField(max_length=20, verbose_name='расчетний счет')),
                ('foto', models.ImageField(upload_to='', verbose_name='фото')),
                ('country', models.CharField(max_length=40, verbose_name='страна')),
                ('city', models.CharField(max_length=40, verbose_name='город')),
                ('street', models.CharField(max_length=40, verbose_name='улица')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='заметка о клиенте')),
                ('phone_number', models.CharField(max_length=20, verbose_name='номер тел.')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('added_user', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='когда')),
                ('update_user', models.DateTimeField(default=django.utils.timezone.now, verbose_name='когда')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='админ')),
            ],
            options={
                'verbose_name': 'Данние клиента',
                'verbose_name_plural': 'Данние клиентов',
            },
        ),
    ]
