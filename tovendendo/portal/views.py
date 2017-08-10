from flask import render_template, Blueprint
from tovendendo.portal.forms import ContactForm


portal = Blueprint('portal', __name__)


@portal.route('/')
@portal.route('/index')
def index():
    return render_template('index.html', user={'email': 'bla@bla.com'})


@portal.route('/about')
def about():
    return render_template('about.html')


@portal.route('/howitworks')
def how_it_works():
    return render_template('how-it-works.html')


@portal.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    # TODO send by email
    return render_template('contact.html', form=form)
