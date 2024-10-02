from django.contrib import admin
from .models import Category, Announcement

# Register your models here.
class AnnouncAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'category', 'address', 'added_time')
    list_display_links=('id', 'title')
    search_fields=('title', 'address')
    list_filter=('category', 'added_time')
    date_hierarchy='added_time'
    ordering=('added_time',)
    list_per_page=20
    list_editable=('category', 'address')
    save_as=True
    save_on_top=True
    readonly_fields=('id', 'added_time')




admin.site.register(Category)
admin.site.register(Announcement, AnnouncAdmin)