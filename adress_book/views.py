from django.shortcuts import render
from adress_book.forms import UserRegistration, ContactAdd


# Create your views here.
def registration(request):
    if request.method == 'POST':
        registration_form = UserRegistration(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            user.set_password(user.password)
            user.save()

    return render(request, 'registration.html')


def add_contact(request):
    if request.method == 'POST':
        contact_info = ContactAdd(data=request.POST)

        if contact_info.is_valid():

            contact_info.save()

    return render(request, 'add_contact.html')
