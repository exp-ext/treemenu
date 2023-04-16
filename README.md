![статус](https://github.com/exp-ext/treemenu/actions/workflows/workflow.yml/badge.svg?event=push)

<div align="center">
    <table border="0" cellpadding="0" cellspacing="0" align="center">
        <tr>
            <td>
                <img src="https://github.com/exp-ext/treemenu/blob/main/treeview/media/tree.png">
            </td>
            <td>
                <img src="https://github.com/exp-ext/treemenu/blob/main/treeview/media/admin.png" class="merge">
            </td>
        </tr>
    </table>
</div>

<div>
<div>Django app, который будет реализовывать древовидное меню, соблюдая следующие условия:</div>
<ol>
<li>Меню реализовано через template tag</li>
<li>Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.</li>
<li>Хранится в БД.</li>
<li>Редактируется в стандартной админке Django</li>
<li>Активный пункт меню определяется исходя из URL текущей страницы</li>
<li>Меню на одной странице может быть несколько. Они определяются по названию.</li>
<li>При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.</li>
<li>На отрисовку каждого меню требуется ровно 1 запрос к БД</li>
</ol>
<div>Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.</div>
<div>&nbsp;</div>

```
{% draw_menu 'main_menu' %}
```

<div>&nbsp;</div>
<div>При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.</div>
</div>
