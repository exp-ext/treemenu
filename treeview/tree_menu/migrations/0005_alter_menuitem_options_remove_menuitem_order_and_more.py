# Generated by Django 4.2 on 2023-04-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0004_remove_menuitem_root_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ('nesting_level',), 'verbose_name': 'Элемент меню', 'verbose_name_plural': 'Элементы меню'},
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='order',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='nesting_level',
            field=models.IntegerField(default=1, verbose_name='Уровень вложенности'),
            preserve_default=False,
        ),
    ]
