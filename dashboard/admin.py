from django.contrib import admin
from .models import dashboard
# from work.models import Kontakt
# from goods.models import goods


# class BbAdmin(admin.ModelAdmin):
#     list_display = ('pasport', 'INN', 'first_name', 'first_name', 'r_r',
#                     'companiName', 'phone_number', 'email', 'city', 'street', 'price',
#                     'name_goods', 'release_date',)
#     list_display_links = ('title', 'content')
#     search_fields = ('pasport', 'INN', 'first_name', 'first_name', 'r_r', 'companiName')


admin.site.register(dashboard)
