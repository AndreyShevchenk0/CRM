from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
User = get_user_model()
# deal firma kanban(доработать)

class Kontakt(models.Model):
    """ Модель Физ.лица """

    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='фамилия')
    age = models.CharField(max_length=2, verbose_name='возраст')
    pasport = models.CharField(max_length=200, verbose_name='серия паспорта')
    INN = models.CharField(max_length=20, verbose_name='инн')  # индификационний номер
    r_r = models.CharField(max_length=20, verbose_name='расчетний счет')  # расщетний счет
    foto = models.ImageField()
    country = models.CharField(max_length=40, verbose_name='страна')
    city = models.CharField(max_length=40, verbose_name='город')
    street = models.CharField(max_length=40, verbose_name='улица')
    title = models.CharField(max_length=200, unique=True, verbose_name='заметка о клиенте')
    phone_number = models.CharField(max_length=20, verbose_name='номер тел.')
    email = models.EmailField(verbose_name='почта')
    added_user = models.DateTimeField(auto_now_add=True, db_index=True,)
    update_user = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    imitation = models.ForeignKey(Firma, on_delete=models.PROTECT)  # наследование полей фирми

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        verbose_name_plural = 'Данние'  # -обьявления
        verbose_name = 'Данние'     # -обьявление
        #ordering = ['name']


class Firma(models.Model):
    """ Модель Юридического.лица """

    #imitation = models.ForeignKey(Kontakt, on_delete=models.PROTECT)  # наследование полей Контакта
    companiName = models.CharField(max_length=40, verbose_name='имя компании')
    logo = models.ImageField(verbose_name='лого')

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        verbose_name_plural = 'Данние'  # -обьявления
        verbose_name = 'Данние'     # -обьявление
        #ordering = ['name']


# class dashboard(models.Model):
#     """ Воронка (карточка клиента + стадии сделки ) создать другое преложение """
#
#     #first_coll = recordsSaund() # доработать
#     #ip = models.GenericIPAddressField()
#     kanban = models.ForeignKey(Kontakt, on_delete=models.CASCADE,)
#     kanban2 = models.ForeignKey(Firma, on_delete=models.CASCADE,)  # возможно many to many
#
#     def __str__(self):
#         return '%s object (%s)' % (self.__class__.__name__, self.pk)
#
#
# class deal(models.Model):
#     """ Сделки - стадии """
#
#     fields_businnes_views_CHOICES = [
#         ('ПЗ', 'Первий звонок'),
#         ('ДК', 'Договор'),
#         ('$', 'Проплата услуги == товара'),
#         ('ПТ', 'Получение товара'),
#     ]
#     #fields_businnes_views = models.
#     time = models.DateTimeField(auto_now_add=True,)
#     kanban = models.ForeignKey(Kontakt, on_delete=models.CASCADE, )
#     kanban2 = models.ForeignKey(Firma, on_delete=models.CASCADE, )
#
#     def __str__(self):
#         return '%s object (%s)' % (self.__class__.__name__, self.pk)
#
#
# class goods(models.Model):
#     """ Товар  = goods (или услуга) """
#
#     #kanban3 = models.ForeignKey(Kontakt, on_delete=models.CASCADE, )
#     #kanban4 = models.ForeignKey(Firma, on_delete=models.CASCADE, )
#     goods_text = models.CharField(max_length=2000, )  # Описание
#     price = models.DecimalField(max_digits=8, decimal_places=4)  # цена
#     name_goods = models.CharField(max_length=100,)   # товар
#     release_date = models.DateField()  # дата
#     #num_stars = models.IntegerField()  #
#
#     def __str__(self):
#         return '%s object (%s)' % (self.__class__.__name__, self.pk)
#
# class settings(models.Model):
#     """  Настройки  CRM  - локальние (Под меню )"""
#
#     pass
#
# class documents(models.Model):
#     """ Перечень всех документов """
#
#     Akt = models.CharField(max_length=4000,)  # 1 Акт
#     # 2 Счет
#     # 3 Счет - Воронка, Карточка
#     # Клиента, Канбан, Список, фактура
#     # 4 Накладная
#     # 5 Довереность
#     # 6 Комерческое предложение
#     # 7 Договор подряда
#     # 8 Договор поставки
#     # 9 Договор оказания услуг
#     # 10 универсальний предаточний документ
#     # 11 Список документов
#     # 12 + Возможность создать свой шаблон +
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