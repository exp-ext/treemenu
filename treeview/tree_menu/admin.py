from django.contrib import admin
from django.db.models import Count

from .models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    ordering = ('slug', 'parent_id')
    list_filter = ('parent',)
    list_display = ('parent', 'title', 'url', 'slug', 'children_count')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (MenuItemInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(children_count=Count('children'))

    def children_count(self, obj):
        return obj.children_count
    children_count.short_description = 'Children count'
    children_count.admin_order_field = 'children_count'
