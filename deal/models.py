from django.db import models
from work.models import Kontakt
from goods.models import goods
from django.utils import timezone
from django.contrib.auth.models import User


class deal(models.Model):
    """ Сделки - стадии """

    CATEGORY = [
        ('перв.звон', 'Первий звонок'),
        ('договор', 'Договор'),
        ('пропл.услу', 'Проплата услуги == товара'),  # Проплата услуги == товара
        ('получ.тов', 'Получение товара'),
    ]

    #slug = models.SlugField(max_length=250, verbose_name='получ.тов')  #  unique_for_date='получение товара',
    time = models.DateTimeField(auto_now_add=True, verbose_name='дата заказа')
    kanban = models.ForeignKey(Kontakt, on_delete=models.CASCADE, verbose_name='имя заказчика')
    status = models.CharField(max_length=10, choices=CATEGORY, default='первий звонок', verbose_name='статус заказа')
    gods = models.ForeignKey(goods, on_delete=models.CASCADE, verbose_name=' список товара покупателя')

    class Meta:
        verbose_name_plural = 'Статус Заказов'
        verbose_name = 'Статус Заказа'
        ordering = ('-status',)

    def __str__(self):
        return self.status
        #return '%s object (%s)' % (self.__class__.__name__, self.pk)

