import flask_login as login
from flask_admin.contrib.sqla import ModelView
from tovendendo.items.models import Item


class ItemView(ModelView):
    form_choices = {'age': Item.TYPES}
    column_hide_backrefs = False
    column_list = ('name', 'price', 'available_on', 'quantity', 'categories', 'pictures')

    def is_accessible(self):
        return login.current_user.is_authenticated


class CategoryView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated
