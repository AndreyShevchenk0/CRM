from django.db import models
from work.models import Kontakt


class documents(models.Model):
    """ Перечень всех документов """

    kanban2 = models.ForeignKey(Kontakt, on_delete=models.CASCADE, verbose_name='наследование конт.')
    Akt = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Акт')
    schet = models.CharField(max_length=200, null=True, blank=True, verbose_name='Счет')
    nakladnay = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Накладная')
    doverinost = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Довереность')
    bussnproposal = models.CharField(max_length=3000, null=True, blank=True, verbose_name='Комерческое предложение')
    podrad = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Договор подряда')
    postavka = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Договор поставки')
    uslugi = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Договор оказания услуг')
    universdok = models.CharField(max_length=2000, null=True, blank=True,
                                  verbose_name='Универсальний предаточний документ')
    listdoks = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Список документов')

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)

    class Meta:
        verbose_name_plural = 'Документ'
        verbose_name = 'Документи'


    #  + Возможность создать свой шаблон + Доработать

