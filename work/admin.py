from django.contrib import admin
from .models import Kontakt, Firma, kanban, deal, goods, settings, documents, HeadMenu


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('first_name', 'first_name', 'age', 'r_r', 'companiName',)

admin.site.register(Kontakt)
admin.site.register(Firma)
admin.site.register(kanban)
admin.site.register(deal)
admin.site.register(goods)
admin.site.register(settings)
admin.site.register(documents)
admin.site.register(HeadMenu)

