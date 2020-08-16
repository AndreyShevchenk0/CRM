from django.contrib import admin
from .models import Kontakt# * settings, HeadMenu


# class BbAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content', 'price', 'published', 'rubric')
#     list_display_links = ('title', 'content')
#     search_fields = ('first_name', 'first_name', 'age', 'r_r', 'companiName')

admin.site.register(Kontakt)
# admin.site.register(deal)
# admin.site.register(settings)
# admin.site.register(HeadMenu)

