"""dms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path("weighbridge/",views.weighbridge,name="wb"),
    path("weighbridge/<int:id>",views.weighbridgeid,name="wb"),
    path("vehicles/",views.vehicles,name="vehicles"),
    path("vehicles/<int:id>",views.vehiclesid,name="vehicles"),
    path("owners/",views.owners,name="owners"),
    path("owners/<int:id>",views.ownersid,name="owners"),
    path("drivers/",views.drivers,name="owners"),
    path("drivers/<int:id>",views.driversid,name="owners"),
    path("locations/",views.locations,name="locations"),
    path("locations/<int:id>",views.locationsid,name="locations"),

]
