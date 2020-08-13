from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
User = get_user_model()


class Kontakt(models.Model):
    """ Модель Физ.лица """
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=2,)
    pasport = models.CharField(max_length=200,)
    INN = models.CharField(max_length=20,)  # индификационний номер
    r_r = models.CharField(max_length=20,)  # расщетний счет
    foto = models.ImageField()
    country = models.CharField(max_length=40,)
    city = models.CharField(max_length=40,)
    street = models.CharField(max_length=40,)
    #records_cols =
    title = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20,)
    email = models.EmailField()
    added_user = models.DateTimeField(auto_now_add=True)
    #update_user = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)


class Firma(models.Model):
    """ Модель Юридического.лица """
    userfirma = models.ForeignKey(Kontakt, on_delete=models.CASCADE, )
    kompani_name = models.CharField(max_length=40)
    logo = models.ImageField()
    country = models.CharField(max_length=40,)
    city = models.CharField(max_length=40,)
    street = models.CharField(max_length=40,)
    INN = models.CharField(max_length=20,)  # индификационний номер
    r_r = models.CharField(max_length=20,)  # расщетний счет
    # records_col =
    title = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20,)
    contact_manager_name = models.CharField(max_length=50,)
    email = models.EmailField()
    added_user = models.DateTimeField(auto_now_add=True)
    update_user = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)


class kanban(models.Model):
    """ Воронка (карточка клиента + стадии сделки )"""

    #first_coll = recordsSaund() # доработать
    #ip = models.GenericIPAddressField()
    kanban = models.ForeignKey(Kontakt, on_delete=models.CASCADE,)
    kanban2 = models.ForeignKey(Firma, on_delete=models.CASCADE,)

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)


class businnesManager(models.Model):
    """ Сделки """
    fields_businnes_views_CHOICES = [
        ('ПЗ', 'Первий звонок'),
        ('ДК', 'Договор'),
        ('$', 'Проплата услуги == товара'),
        ('ПТ', 'Получение товара'),
    ]
    #fields_businnes_views = models.
    time = models.DateTimeField(auto_now_add=True,)
    kanban = models.ForeignKey(Kontakt, on_delete=models.CASCADE, )
    kanban2 = models.ForeignKey(Firma, on_delete=models.CASCADE, )

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)


class goods(models.Model):
    """ Товар  = goods (или услуга) """
    kanban3 = models.ForeignKey(Kontakt, on_delete=models.CASCADE, )
    kanban4 = models.ForeignKey(Firma, on_delete=models.CASCADE, )
    goods_text = models.CharField(max_length=2000, )  # Описание
    price = models.DecimalField(max_digits=8, decimal_places=4)
    name_goods = models.CharField(max_length=100,)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

class settings(models.Model):
    """  Настройки  CRM  - локальние (Под меню )"""
    pass

class documents(models.Model):
    """ Перечень всех документов """
    Akt = models.CharField(max_length=4000,)  # 1 Акт
    # 2 Счет
    # 3 Счет - Воронка, Карточка
    # Клиента, Канбан, Список, фактура
    # 4 Накладная
    # 5 Довереность
    # 6 Комерческое предложение
    # 7 Договор подряда
    # 8 Договор поставки
    # 9 Договор оказания услуг
    # 10 универсальний предаточний документ
    # 11 Список документов
    # 12 + Возможность создать свой шаблон +
    pass


class HeadMenu(models.Model):
    """ Главное Меню """
    # 1.Почта
    # 2.CRM
    # 3.Контакт центр
    # 4.СRM - Воронка, Карточка Клиента, Канбан, Список, аналитика
    # 5.Задачи и проекти
    # 6.Настройки
    pass