from django import forms
from django.contrib.auth.models import User
from adress_book.models import ContactInfo


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ContactAdd(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'
