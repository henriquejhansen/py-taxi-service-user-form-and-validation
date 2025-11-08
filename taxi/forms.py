from django import forms
from django.core.exceptions import ValidationError
from .models import Driver, Car

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['username', 'first_name', 'last_name', 'license_number']

class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['license_number']

    def clean_license_number(self):
        license = self.cleaned_data['license_number']
        if len(license) != 8 or not license[:3].isalpha() or not license[:3].isupper() or not license[3:].isdigit():
            raise ValidationError("License must be 3 uppercase letters followed by 5 digits.")
        return license

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'manufacturer', 'drivers']
        widgets = {
            'drivers': forms.CheckboxSelectMultiple()
        }
