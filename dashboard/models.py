from django.db import models
from goods.models import goods
from work.models import Kontakt
from deal.models import deal


class dashboard(models.Model):
    """ Воронка (карточка клиента + стадии сделки )  """

    view = models.ForeignKey(goods, on_delete=models.CASCADE, verbose_name='Tовар')
    view1 = models.ForeignKey(Kontakt, on_delete=models.CASCADE, verbose_name='Покупатель')
    view2 = models.ForeignKey(deal, on_delete=models.CASCADE, verbose_name='Статус сделки')
    title2 = models.CharField(max_length=200, unique=True, verbose_name='Запись менеджера о погоде')

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        verbose_name_plural = 'Воронка'
        verbose_name = 'Воронку'


