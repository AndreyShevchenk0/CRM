from django.contrib import admin
from .models import deal


@admin.register(deal)
class BbAdmin(admin.ModelAdmin):
    list_display = ('status', 'gods', 'kanban', 'time')
    list_display_links = ('status', 'gods', 'kanban')
    search_fields = ('status', 'gods', 'kanban')
