from django.test import Client, TestCase
from django.urls import reverse

from .models import MenuItem
from .templatetags.draw_menu import render_menu


class DrawMenuTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_item_1 = MenuItem.objects.create(
            title='Menu Item 1',
            slug='main_menu',
            url='/1/'
        )
        self.menu_item_2 = MenuItem.objects.create(
            title='Menu Item 2',
            slug='main_menu',
            url='/2/',
            parent=self.menu_item_1
        )
        self.menu_item_3 = MenuItem.objects.create(
            title='Menu Item 3',
            slug='main_menu',
            url='/3/',
            parent=self.menu_item_2
        )
        self.menu_item_4 = MenuItem.objects.create(
            title='Menu Item 4',
            slug='main_menu',
            url='/4/',
            parent=self.menu_item_3
        )

    def test_render_menu(self):
        menu_items = MenuItem.objects.all()
        menu_dict = render_menu(menu_items)
        expected_dict = {
            self.menu_item_1: {
                self.menu_item_2: {
                    self.menu_item_3: {
                        self.menu_item_4: {}
                    }
                }
            }
        }
        self.assertEqual(menu_dict, expected_dict)

    def test_draw_menu(self):
        response = self.client.get(reverse('tree_menu:tree_menu'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Menu Item 1')
        self.assertContains(response, 'Menu Item 2')
        self.assertContains(response, 'Menu Item 3')
        self.assertContains(response, 'Menu Item 4')

    def test_post_active(self):
        response = self.client.get(reverse('tree_menu:post_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            f'<a class="active" href="{self.menu_item_1.url}">'
        )
        self.assertContains(response, 'Элемент-1')
        self.assertContains(response, 'Menu Item 1')
