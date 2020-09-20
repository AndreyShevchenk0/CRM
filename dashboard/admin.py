from django.contrib import admin
from .models import dashboard
from goods.models import goods
from work.models import Kontakt
from deal.models import deal


# class BbAdmin(admin.ModelAdmin):
#     list_display = ('pasport', 'INN', 'first_name', 'first_name', 'r_r',
#                     'companiName', 'phone_number', 'email', 'city', 'street', 'price',
#                     'name_goods', 'release_date',)
#     list_display_links = ('title', 'content')
#     search_fields = ('pasport', 'INN', 'first_name', 'first_name', 'r_r', 'companiName')


#admin.site.register(dashboard)

@admin.register(dashboard)
class BbAdmin(admin.ModelAdmin):
    list_display = ('view', 'view1', 'view2', 'title2')
    list_display_links = ('view', 'view1', 'view2', 'title2')
    search_fields = ('view', 'view1', 'view2', 'title2')
