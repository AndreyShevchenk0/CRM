from django.contrib import admin
from .models import deal
#from goods.models import goods  # может лишнее
#from work.models import Kontakt  # может лишнее


@admin.register(deal)
class BbAdmin(admin.ModelAdmin):
    list_display = ('status', 'gods', 'kanban', 'time')
    list_display_links = ('status', 'gods', 'kanban')
    search_fields = ('status', 'gods', 'kanban')



""" фильтр 20% """
    # @admin.register(Product)
    # class ProductAdmin(admin.ModelAdmin):
    #     list_display = ('name_product', 'price')
    #     actions = ['discount_20']
    #
    #     def discount_20(self, request, queryset):
    #         from math import ceil
    #         discount = 20  # percentage
    #
    #         for product in queryset:
    #             """ Set a discount of 20% to selected products """
    #             multiplier = discount / 100.  # discount / 100 in python 3
    #             old_price = product.price
    #             new_price = ceil(old_price - (old_price * multiplier))
    #             product.price = new_price
    #             product.save(update_fields=['price'])
    #
    #     discount_20.short_description = 'Set 20%% discount'
