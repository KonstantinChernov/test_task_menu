from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu/tags/recursive_menu.html', takes_context=True)
def draw_menu(context, root_item_url):

    path_to_item = []

    # В эту переменную передаем корень конкретного меню на случай если несколько меню на странице
    root_menu_url = root_item_url

    def create_path(item):
        """
        Ф-ция рекурсивно отслеживает путь от выбранного пункта меню
        до корня дерева и записывает элементы-родители в список path_to_item
        :param item: пункт меню, объект модели Menu
        :return:
        """
        path_to_item.append(item)
        if item.parent:
            create_path(item.parent)

    # Забираем выбранный пользоватем пункт меню из get-параметра item из url
    chosen_item = context['request'].GET.get('item')
    if not chosen_item:
        try:
            root_item = Menu.objects.get(url=root_item_url)
        except Menu.DoesNotExist:
            root_item = None

    # Если get-параметр был в url, пытаемся вытащить из модели Menu соответствующий объект
    # с помощью ф-ции create_path находим всех родителей, выбираем первого как корневой
    else:
        chosen_item = Menu.objects.get(url=chosen_item)
        create_path(chosen_item)
        root_item = path_to_item[-1]

    # Сравниваем корневую ноду конкретного дерева-меню с корневой нодой на прошлом шаге
    # для разграничения работы разных меню (Это дополнительный запрос к БД).
    if root_item.url != root_menu_url:
        try:
            root_item = Menu.objects.get(url=root_item_url)
        except Menu.DoesNotExist:
            root_item = None

    return {
        "root_item": root_item,
        "list_of_parents": path_to_item,
        "root_menu_url": root_menu_url
    }
