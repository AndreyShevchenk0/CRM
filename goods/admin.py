from django.contrib import admin
from .models import goods


@admin.register(goods)
class BbAdmin(admin.ModelAdmin):
    list_display = ('name_goods', 'price')
    list_display_links = ('name_goods', 'price')
    search_fields = ('name_goods', 'price')
