# Generated by Django 4.2 on 2023-04-12 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Родительский пункт меню')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug меню')),
            ],
            options={
                'verbose_name': 'Родительский пункт меню',
                'verbose_name_plural': 'Родительский пункт меню',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
                ('order', models.IntegerField(verbose_name='Порядковый номер')),
                ('parent_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tree_menu.menu', verbose_name='Родительский пункт меню')),
            ],
            options={
                'verbose_name': 'Элемент меню',
                'verbose_name_plural': 'Элементы меню',
            },
        ),
    ]
