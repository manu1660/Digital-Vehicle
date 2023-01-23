"""digitalvehicle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from digiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login),
    path('rto', views.rto),
    path('insurance', views.insurance),
    path('pollution', views.pollution),
    path('police', views.police),

    path('adminhome', views.adminhome),
    path('adminrto', views.adminrto),
    path('adminpollution', views.adminpollution),
    path('adminpolice', views.adminpolice),
    path('admininsurance', views.admininsurance),
    path('adminupdateuser', views.updateuser),
    path('adminfeedback', views.adminfeedback),

    path('rtohome', views.rtohome),
    path('rtoaddvehicle', views.rtoaddvehicle),
    path('rtoviewvehicle', views.rtoviewvehicle),
    path('rtoownership', views.rtoownership),
    

    path('customerhome', views.customerhome),
    path('customerinsurance', views.customerinsurance),
    path('payment', views.payment),
    path('customercase', views.customercase),
    path('payment1', views.payment1),
    path('customerfeedback', views.customerfeedback),

    path('insurancehome', views.insurancehome),
    path('insurancerenew', views.insurancerenew),
    path('getinsurance', views.getinsurance),
    path('insurancedetails', views.insurancedetails),

    path('pollutionhome', views.pollutionhome),
    path('pollutionrenew', views.pollutionrenew),
    path('getpollution', views.getpollution),
    path('pollutiondetails', views.pollutiondetails),

    path('policehome', views.policehome),
    path('findvehicle', views.findvehicle),
    path('policecase', views.policecase),
    path('policecasestatus', views.policecasestatus),
]
