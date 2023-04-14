from django import template

from ..models import MenuItem

register = template.Library()


def render_menu(menu_items, parent=None):
    """
    Рекурсивно создаёт словарь древовидного меню.
    """
    menu_dict = {}
    for item in menu_items:
        if item.parent == parent:
            sub_menu = render_menu(menu_items, item)
            if sub_menu:
                menu_dict[item] = sub_menu
            else:
                menu_dict[item] = {}
    return menu_dict


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Одним запросом выгружаем queryset с данными для меню
    создаём и возвращаем словарь и текущий url.
    """

    menu_items = MenuItem.objects.filter(
        slug=menu_name
    ).select_related('parent')

    menu_dict = render_menu(menu_items)

    if menu_dict:
        context = {
            'menu_dict': menu_dict,
            'current_url': context['request'].path,
        }
        return context
