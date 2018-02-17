from django.shortcuts import render
from adress_book.forms import UserRegistration


# Create your views here.
def registration(request):
    if request.method == 'POST':
        registration_form = UserRegistration(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            user.set_password(user.password)
            user.save()

    return render(request, 'registration.html')
