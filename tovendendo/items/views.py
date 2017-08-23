import flask_login as login
from flask_admin.contrib.sqla import ModelView
from flask_admin.model.fields import InlineFieldList
from flask_admin.form import ImageUploadField
from flask import Markup

from tovendendo.items.models import Item, Picture


def _list_thumbnail(view, context, model, name):
    if not model.pictures:
        return ''

    return Markup(
        '<img src="{model.pictures}" style="width: 150px;">'.format(model=model)
    )


class ItemView(ModelView):
    form_choices = {'age': Item.TYPES}
    column_hide_backrefs = False
    column_list = ('name', 'price', 'available_on', 'quantity', 'categories', 'pictures')
    form_extra_fields = {
        'pictures': InlineFieldList(
            ImageUploadField('Picture', base_path='data/images', url_relative_path='images/',))}
    column_formatters = {
        'pictures': _list_thumbnail
    }

    def create_model(self, form):
        # FIXME multiple image upload is not working :(
        base_path = 'data/'

        pictures = []
        for picture in form.pictures.data:
            filename = base_path + picture.filename
            picture.save(filename)
            pictures.append(Picture(name=picture.filename, filename=filename))

        form.pictures = pictures
        super(ItemView, self).create_model(form)

    def is_accessible(self):
        return login.current_user.is_authenticated


# TODO create structure to is_accessible - to avoid duplicated code
class CategoryView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated
