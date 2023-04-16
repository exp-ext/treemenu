from typing import Dict, List, Optional
from django import template

from ..models import MenuItem

register = template.Library()


def render_menu(menu_items: List[MenuItem],
                parent: Optional[MenuItem] = None) -> Dict[MenuItem, Dict]:
    """
    Рекурсивно создаёт словарь для древовидного меню.

    :param menu_items: queryset MenuItem, для которых необходимо
    создать меню
    :param parent: опциональный объект MenuItem, родительский элемент
    :return: словарь, представляющий древовидное меню, где ключ - объект
    MenuItem, значение - словарь с дочерними элементами
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
def draw_menu(context: Dict, menu_name: str) -> Dict:
    """
    Одним запросом выгружаем queryset с данными для меню,
    инициирует создание и возвращаем словарь с меню и текущий url.

    :param context: словарь контекста, содержащий информацию об HTTP-запросе
    :param menu_name: строковое значение, slag для фильтрации меню
    :return: Словарь, содержащий древовидное меню; текущий URL.
    """
    menu_items = (
        MenuItem.objects.filter(slug=menu_name).select_related('parent')
    )

    menu_dict = render_menu(menu_items)

    if menu_dict:
        context = {
            'menu_dict': menu_dict,
            'current_url': context['request'].path,
        }
        return context
