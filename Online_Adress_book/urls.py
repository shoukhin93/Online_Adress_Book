"""Online_Adress_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adress_book import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/', views.user_registration, name='registration'),
    path('addContact/', views.add_contact, name='Add Contact'),
    path('addPhone/<int:id>/', views.add_phone_number, name='Add Phone Number'),
    path('deletePhone/<int:id>/', views.delete_phone_number, name='Delete Phone Number'),
    path('updatePhone/<int:id>/', views.update_phone_number, name='Update Phone Number'),
    path('updateContact/<int:id>/', views.update_contact_info, name='Update Contact info'),
    path('deleteContact/<int:id>/', views.delete_contact_info, name='Delete Contact info'),
    path('uploadCSV/', views.upload_csv, name="upload_csv"),
    path('downloadCSV/<int:id>/', views.download_csv_file, name="download_csv"),
    path('admin/', admin.site.urls),
]
