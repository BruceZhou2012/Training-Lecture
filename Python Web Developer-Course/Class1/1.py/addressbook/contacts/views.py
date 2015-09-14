# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from .models import Contact
from django.views.generic import DetailView
import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
# FBV
# def hello_world(request):
#    return HttpResponse("hello,workd")

# CBV

class ContactOwnerMixin(object):

    def get_object(self, queryset=None):
        """Returns the object the view is displaying.

        """
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied

        return obj

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class MyVIew(View):

    def get(self, request):
        return HttpResponse("hello,world")

class ListContactView(LoggedInMixin, ListView):

    model = Contact
    template_name = 'contact_list.html'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class CreateContactView(CreateView):

    model = Contact
    template_name = 'contacts/edit_contact.html'
    form_class =  forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context

class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'contacts/edit_contact.html'
    form_class =  forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        #print context
        context['action'] = reverse('contacts-edit',kwargs={'pk':self.get_object().id})
        print context['action']
        return context

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'contacts/delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')


class ContactView(LoggedInMixin, ContactOwnerMixin, DetailView):

    model = Contact
    template_name = 'contacts/contact.html'


class EditContactAddressView(UpdateView):

    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.ContactAddressFormSet

    def get_success_url(self):

        # redirect to the Contact view.
        return self.get_object().get_absolute_url()