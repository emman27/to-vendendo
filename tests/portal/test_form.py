from tovendendo.portal.forms import ContactForm
import pytest


def test_contact_form_is_valid(client):
    form = ContactForm(name='Maria', email='m@ria.com', phone_number='89898989')

    assert form.validate()


@pytest.mark.parametrize('name,email,phone_number', [
    ('', '', ''),
    (None, None, None),
    ('pe', 'que', 'no'),
])
def test_contact_form_is_invalid(client, name, email, phone_number):
    form = ContactForm(name=name, email=email, phone_number=phone_number)

    assert not form.validate()
