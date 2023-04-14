from django.db import models


class MenuItem(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name='slug меню'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родительский пункт меню'
    )
    url = models.CharField(
        max_length=200,
        verbose_name='URL'
    )

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return self.title
