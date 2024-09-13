from django import forms
from django.forms import fields, widgets
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'telefono',
            'celular',
            'correo',
            'url'
        ]
        widgets = {
            'correo': forms.EmailInput(),
            'url': forms.URLInput()
        }

class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = [
            'pais',
            'estado',
            'ciudad',
            'colonia',
            'cp',
            'calle',
            'ne',
            'ni'
        ]
        widgets = {'__all__'}

class FiscalForm(forms.ModelForm):
    class Meta:
        model = Fiscal
        fields = [
            'rfc',
            'rs'
        ]
        widgets = {'__all__'}

class NegocioForm(forms.ModelForm):
    class Meta:
        model = Negocio
        fields = [
            'nombre'
        ]
        widgets = {'__all__'}

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']
        widgets = {'__all__'}

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellidos'
        ]
        widgets = {'__all__'}

class CajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = [
            'clave',
            'nombre'
        ]
        widgets = {'__all__'}

class DepartamanetoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre']
        widgets = {'__all__'}

class MedidaForm(forms.ModelForm):
    class Meta:
        model = Medida
        fields = ['nombre']
        widgets = {'__all__'}

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'marca',
            'existencia',
            'departamento',
            'precio',
            'existencia_minima'
        ]
        widgets = {
            'descripcion': forms.Textarea(),
            'existencia': forms.NumberInput(),
            'precio': forms.NumberInput(),
            'existencia_minima': forms.NumberInput(),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'apellidos',
            'genero',
            'rol',
        ]
        widgets = {'__all__'}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput()
        }
    def clean_password(self):
        password = self.cleaned_data['password']  

        return make_password(password)
    
class EmployeForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'apellidos',
            'genero',
        ]
        widgets = {'__all__'}

class MCajaForm(forms.ModelForm):
    class Meta:
        model = MovimentoCaja
        fields = [
            'monto_abierto',
            'monto_cierre',
        ]
        widgets = {
            'monto_abierto': forms.NumberInput(),
            'monto_cierre': forms.NumberInput(),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'producto',
            'cantidad',
            'descuento'
        ]
        widgets = {'__all__'}