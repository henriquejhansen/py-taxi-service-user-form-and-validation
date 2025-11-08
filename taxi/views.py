from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from .models import Driver, Car
from .forms import DriverForm, DriverLicenseUpdateForm, CarForm

class DriverCreateView(generic.CreateView):
    model = Driver
    form_class = DriverForm
    template_name = "taxi/driver_form.html"
    success_url = reverse_lazy("taxi:driver-list")

class DriverDeleteView(generic.DeleteView):
    model = Driver
    template_name = "taxi/driver_confirm_delete.html"
    success_url = reverse_lazy("taxi:driver-list")

class DriverLicenseUpdateView(generic.UpdateView):
    model = Driver
    form_class = DriverLicenseUpdateForm
    template_name = "taxi/driver_license_form.html"
    success_url = reverse_lazy("taxi:driver-list")

class CarUpdateView(generic.UpdateView):
    model = Car
    form_class = CarForm
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")

def assign_driver_to_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.drivers.add(request.user)
    return redirect("taxi:car-detail", pk=pk)

def remove_driver_from_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.drivers.remove(request.user)
    return redirect("taxi:car-detail", pk=pk)
