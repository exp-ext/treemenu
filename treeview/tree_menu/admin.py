from django.contrib import admin

from .forms import MenuItemForm
from .models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
    form = MenuItemForm


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    ordering = ('slug',)
    list_display = ('parent', 'title', 'url', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (MenuItemInline,)
