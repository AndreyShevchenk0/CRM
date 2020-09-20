from django.contrib import admin
from .models import Kontakt# * settings, HeadMenu


@admin.register(Kontakt)
class BbAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'companiName', 'pasport', 'INN', 'city', 'phone_number', 'title')
    list_display_links = ('name_user', 'companiName', 'pasport', 'INN', 'city', 'phone_number')
    search_fields = ('name_user', 'companiName', 'pasport', 'INN', 'city', 'phone_number')

#admin.site.register(Kontakt)

# admin.site.register(deal)
# admin.site.register(settings)
# admin.site.register(HeadMenu)


# list_display = ('title', 'slug', 'author', 'publish','status')
# list_filter = ('status', 'created', 'publish', 'author')
# search_fields = ('title', 'body')
# prepopulated_fields = {'slug': ('title',)}
# raw_id_fields = ('author',)
# date_hierarchy = 'publish'
# ordering = ('status', 'publish')

