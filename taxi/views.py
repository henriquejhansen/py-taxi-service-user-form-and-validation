from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import DriverForm, DriverLicenseUpdateForm, CarForm
from .models import Car

Driver = get_user_model()


# Página inicial opcional
class HomeView(generic.TemplateView):
    template_name = "taxi/home.html"


# Motoristas

class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"


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


# Carros

class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car"


class CarUpdateView(generic.UpdateView):
    model = Car
    form_class = CarForm
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")


# Atribuição de motorista ao carro

def assign_driver_to_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.drivers.add(request.user)
    return redirect("taxi:car-detail", pk=pk)


def remove_driver_from_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.drivers.remove(request.user)
    return redirect("taxi:car-detail", pk=pk)
