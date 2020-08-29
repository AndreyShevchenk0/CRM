from django.db import models
from work.models import Kontakt


class deal(models.Model):
    """ Сделки - стадии """

    CATEGORY = [
        ('ПЗ', 'Первий звонок'),
        ('ДК', 'Договор'),
        ('$', 'Проплата услуги == товара'),
        ('ПТ', 'Получение товара'),
    ]

    time = models.DateTimeField(auto_now_add=True,)
    kanban = models.ForeignKey(Kontakt, on_delete=models.CASCADE, choices=CATEGORY, verbose_name='статус заказа')

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        verbose_name_plural = 'Статус Заказов'
        verbose_name = 'Статус Заказа'
#(*)

