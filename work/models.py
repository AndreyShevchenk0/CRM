from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
User = get_user_model()

class Kontakt(models.Model):
    """ Модель Физ.лица  + Юр.лица """

    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, verbose_name='админ')
    first_name = models.CharField(max_length=40, verbose_name='имя и отчество')
    last_name = models.CharField(max_length=20, verbose_name='фамилия')
    companiName = models.CharField(max_length=40, verbose_name='имя компании')
    logo = models.ImageField(verbose_name='лого')
    age = models.CharField(max_length=2, verbose_name='возраст')
    pasport = models.CharField(max_length=200, verbose_name='серия паспорта')
    INN = models.CharField(max_length=20, verbose_name='инн')  # индификационний номер
    r_r = models.CharField(max_length=20, verbose_name='расчетний счет')  # расщетний счет
    foto = models.ImageField(verbose_name='фото')
    country = models.CharField(max_length=40, verbose_name='страна')
    city = models.CharField(max_length=40, verbose_name='город')
    street = models.CharField(max_length=40, verbose_name='улица')
    title = models.CharField(max_length=200, unique=True, verbose_name='заметка о клиенте')
    phone_number = models.CharField(max_length=20, verbose_name='номер тел.')
    email = models.EmailField(verbose_name='почта')
    added_user = models.DateTimeField(auto_now_add=True, db_index=True)
    update_user = models.DateTimeField(default=timezone.now, verbose_name='когда')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        verbose_name_plural = 'Данние клиентов'  # -обьявления
        verbose_name = 'Данние клиента'     # -обьявление
        #ordering = ['name']


# class settings(models.Model):
#     """  Настройки  CRM  - локальние (Под меню )"""
#
#     pass
#
#
# class HeadMenu(models.Model):
#     """ Главное Меню """
#
#     # 1.Почта
#     # 2.CRM
#     # 3.Контакт центр
#     # 4.СRM - Воронка, Карточка Клиента, Канбан, Список, аналитика
#     # 5.Задачи и проекти
#     # 6.Настройки
#     pass

# Альтернатива**********************************************************************************
# class Customer(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_create = models.DateTimeField(auto_now_add=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     CATEGORY = (
#         ('Indoor', 'Indoor'),
#         ('Out Door', 'Out Door'),
#     )
#     name = models.CharField(max_length=200, null=True)
#     price = models.FloatField(null=True)
#     category = models.CharField(max_length=200, null=True, choices=CATEGORY)
#     description = models.CharField(max_length=200, null=True, blank=True)
#     date_create = models.DateTimeField(auto_now_add=True, null=True)
#     tags = models.ManyToManyField(Tag)
#
#     def __str__(self):
#         return self.name
#
#
# class Order(models.Model):
#     STATUS = (
#         ('Pending', 'Pending'),
#         ('Out for delivery', 'Out for delivery'),
#         ('Delivered', 'Delivered'),
#     )
#     customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
#     product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
#     date_create = models.DateTimeField(auto_now_add=True, null=True)
#     status = models.CharField(max_length=200, null=True, choices=STATUS)
#
#     # def __str__(self):
#     #     return self.name
#
#
# class Tag(models.Model):
#     name = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.name