from django.urls import path
from . import views

app_name = "taxi"

urlpatterns = [
    path("drivers/create/", views.DriverCreateView.as_view(), name="driver-create"),
    path("drivers/<int:pk>/delete/", views.DriverDeleteView.as_view(), name="driver-delete"),
    path("drivers/<int:pk>/update-license/", views.DriverLicenseUpdateView.as_view(), name="driver-update-license"),
    path("cars/<int:pk>/assign/", views.assign_driver_to_car, name="car-assign"),
    path("cars/<int:pk>/remove/", views.remove_driver_from_car, name="car-remove"),
]
