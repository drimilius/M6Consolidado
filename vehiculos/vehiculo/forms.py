
from django import forms
from .models import Vehiculo  

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo  
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']  # Los campos que necesitas
        widgets = {
            'marca': forms.Select(choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')]),
            'categoria': forms.Select(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')]),
        }
