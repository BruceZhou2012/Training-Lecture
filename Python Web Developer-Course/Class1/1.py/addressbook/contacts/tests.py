from django.test import TestCase
from .models import Contact
from django.test.client import  Client
from rebar.testing import flatten_to_dict
from contacts import forms

'''
class ContactTest(TestCase):

    def test_str(self):
        contact = Contact(first_name='baoer',last_name='gu')
        self.assertEquals(str(contact),'gubaoer',)

class ContactListViewTests(TestCase):

    def test_contacts_in_the_context(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(list(response.context['object_list']),[])
        Contact.objects.create(first_name='gu',last_name='baoer')
        response = client.get('/')
        self.assertEquals(response.context['object_list'].count(),1)
'''

class EditContactFormTests(TestCase):

    def test_mismatch_email_is_invalid(self):
        form_data = flatten_to_dict(forms.ContactForm())
        form_data['first_name'] = 'baoer'
        form_data['last_name'] = 'gu'
        form_data['email'] = 'gubaoer@example.com'
        form_data['confirm_email'] = 'gubaoer@example.com'
        bound_form = forms.ContactForm(data=form_data)
        self.assertFalse(bound_form.is_valid())

