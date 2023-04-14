from django.contrib import admin

from .forms import MenuItemForm
from .models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
    form = MenuItemForm


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    ordering = ('slug', 'parent_id')
    list_filter = ('parent_id',)
    list_display = ('parent', 'title', 'url', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (MenuItemInline,)
