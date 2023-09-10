from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("railwaysiding/",views.RailwaySiding.as_view(),name="railwaysiding"),
    path("railwaysiding/<int:id>",views.RailwaySidingId.as_view(),name="railwaysiding"),
    path("ingate/",views.InGate.as_view(),name="ingate"),
    path("ingate/<int:id>",views.InGateId.as_view(),name="ingate"),
    path("outgate/",views.OutGate.as_view(),name="outgate"),
    path("outgate/<int:id>",views.OutGateId.as_view(),name="outgate"),
    path("fuelgate/",views.FuelGate.as_view(),name="fuelgate"),
    path("fuelgate/<int:id>",views.FuelGateId.as_view(),name="fuelgate"),
]
