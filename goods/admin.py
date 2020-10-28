from django.contrib import admin
from .models import goods


@admin.register(goods)
class BbAdmin(admin.ModelAdmin):
    list_display = ('name_goods', 'quantity_goods_stock', 'price', 'release_date')
    list_display_links = ('name_goods', 'quantity_goods_stock', 'price')
    search_fields = ('name_goods', 'quantity_goods_stock', 'price')
