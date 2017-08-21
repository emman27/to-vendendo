from tovendendo.db import db
from sqlalchemy_utils import ChoiceType
from flask_uploads import UploadSet, IMAGES


items = db.Table(
    'categories_items',
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('items.id'))
)

images = UploadSet('images', IMAGES)


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
    pictures = db.relationship('Picture', backref='items')

    def __repr__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Picture(db.Model):
    __tablename__ = 'pictures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    filename = db.Column(db.String(128), unique=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    def __repr__(self):
        return '%r' % (self.filename)

    @property
    def url(self):
        return images.url(self.filename)

    @property
    def filepath(self):
        if self.filename is None:
            return
        return images.path(self.filename)
