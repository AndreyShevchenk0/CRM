from django.db import models
from work.models import Kontakt

# Склад товара
class goods(models.Model):
    """ Товар  = goods (или услуга) """

    kanban1 = models.ForeignKey(Kontakt, blank=False,  on_delete=models.CASCADE, verbose_name='наследование конт.')

    name_goods = models.CharField(max_length=100, verbose_name='товар или услуга')
    quantity_goods_stock = models.CharField(max_length=15, verbose_name='товар в наличии на складе')
    goods_text = models.CharField(max_length=2000, verbose_name='описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    release_date = models.CharField(max_length=100, verbose_name='дата возможной поставки товара клиенту')

    def __str__(self):
        return self.name_goods
        #return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        verbose_name_plural = 'Товари - Услуги'
        verbose_name = 'Товар - Услуга'

