from django.shortcuts import render
from adress_book.forms import UserRegistration, ContactAdd, MobileNumberSave
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from adress_book.models import ContactInfo, MobileNumber
from django.contrib.auth.models import User


# Create your views here.

def index(request):

    if request.user.is_authenticated:

        contacts = ContactInfo.objects.all()
        user = User.objects.get(username__exact=request.user.username)
        return render(request, 'user_home.html', context={'user': user})

    else:
        return render(request, 'user_home.html')


def user_login(request):
    """ Method to get a user logged in"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        else:
            return HttpResponse("invalid username or password")

    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_registration(request):
    if request.method == 'POST':
        registration_form = UserRegistration(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            user.set_password(user.password)
            user.save()

    return render(request, 'registration.html')


def add_contact(request):
    print(request.user)

    if request.method == 'POST':

        if request.user.is_authenticated:

            contact_info = ContactAdd(request.POST)

            if contact_info.is_valid():

                info = contact_info.save(commit=False)
                info.user_name = request.user
                info.save()

                phone = MobileNumberSave(request.POST)

                phone_number = phone.save(commit=False)
                phone_number.phone_id = info
                phone_number.save()

                return HttpResponseRedirect(reverse('index'))
            else:
                print(contact_info.errors)
                return HttpResponse("invalid data!")

        else:
            return HttpResponse("u r not logged in")
    else:
        return render(request, 'add_contact.html')
