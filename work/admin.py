from django.contrib import admin
from .models import Kontakt, Firma, kanban, businnesManager, goods, settings, documents, HeadMenu

admin.site.register(Kontakt)
admin.site.register(Firma)
admin.site.register(kanban)
admin.site.register(businnesManager)
admin.site.register(goods)
admin.site.register(settings)
admin.site.register(documents)
admin.site.register(HeadMenu)

