from tovendendo.db import db
from sqlalchemy_utils import ChoiceType
from flask_admin.contrib.sqla import ModelView


items = db.Table(
    'categories_items',
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('items.id'))
)


class Item(db.Model):
    TYPES = [
        ('six-months', '0 ~ 6 months'),
        ('six-months-one-year', '6 months ~ 1 year'),
        ('one-year-two-years', '1 year ~ 2 years'),
        ('greater-than-two-years', 'Greater than 2 years')
    ]

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    description = db.Column(db.String(255))
    manufacturer = db.Column(db.String(100))
    price = db.Column(db.Float, default=0.0)
    age = db.Column(ChoiceType(TYPES, impl=db.String()), default='six-months-one-year')
    available_on = db.Column(db.DateTime())
    quantity = db.Column(db.Integer, default=1, nullable=False)
    categories = db.relationship(
        'Category', secondary=items, backref=db.backref('items', lazy='dynamic'))

    def __repr__(self):
        return 'Item %r' % (self.name)


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '%r' % (self.name)


class ItemView(ModelView):
    form_choices = {'age': Item.TYPES}
    column_hide_backrefs = False
    column_list = ('name', 'price', 'available_on', 'quantity', 'categories')
