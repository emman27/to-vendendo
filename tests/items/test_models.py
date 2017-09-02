from tovendendo.items.models import Item, Category


def test_show_item_name():
    data = {'name': 'TV/Monitor Samsung'}
    assert repr(Item(**data)) == 'TV/Monitor Samsung'


def test_show_category():
    data = {'name': 'Eletronics'}
    assert repr(Category(**data)) == 'Eletronics'
