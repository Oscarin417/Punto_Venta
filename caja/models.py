from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacto(models.Model):
    telefono = models.CharField(max_length=10, null=True, blank=True)
    celular = models.CharField(max_length=10, null=False, blank=False)
    correo = models.EmailField(null=False, blank=False)
    url = models.URLField(null=True, blank=True)

class Domicilio(models.Model):
    pais = models.CharField(max_length=20, null=False, blank=False)
    estado = models.CharField(max_length=20, null=False, blank=False)
    ciudad = models.CharField(max_length=20, null=False, blank=False)
    colonia = models.CharField(max_length=20, null=False, blank=False)
    cp = models.CharField(max_length=5, null=False, blank=False, verbose_name='Codigo postal')
    calle = models.CharField(max_length=20, null=False, blank=False)
    ne = models.CharField(max_length=10, null=False, blank=False, verbose_name='Numero exterior')
    ni = models.CharField(max_length=10, null=True, blank=True, verbose_name='Numero interior')

class Fiscal(models.Model):
    rfc = models.CharField(max_length=8, null=False, blank=False)
    rs = models.CharField(max_length=30, null=False, blank=False, verbose_name='Razon social')
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

class Negocio(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    contacto = models.ForeignKey(Contacto, on_delete=models.SET_NULL, null=True)
    fiscal = models.ForeignKey(Fiscal, on_delete=models.SET_NULL, null=True)

class Empleado(models.Model):
    GENERO = [
        ('', 'Seleccione una opcion'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    ROL = [
        ('', 'Seleccione un rol'),
        ('A', 'Administrador'),
        ('E', 'Empleado')
    ]
    nombre = models.CharField(max_length=40, null=False, blank=False, verbose_name='Nombre(s)')
    apellidos = models.CharField(max_length=40, null=False, blank=False)
    genero = models.CharField(max_length=1, choices=GENERO, null=False, blank=False)
    rol = models.CharField(max_length=1, choices=ROL, null=False, blank=False, default='E')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contacto = models.ForeignKey(Contacto, on_delete=models.SET_NULL, null=True)
    def genero_c(self):
        genero = ''
        
        if self.genero == 'M':
            genero = 'Masculino'
        else:
            genero = 'Femenino'

        return genero
    
    def rol_c(self):
        rol = ''

        if self.rol == 'E':
            rol = 'Empleado'
        else:
            rol = 'Administrador'

        return rol

class Marca(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=40, null=False, blank=False, verbose_name='Nombre(s)')
    apellidos = models.CharField(max_length=40, null=False, blank=False)
    contacto = models.ForeignKey(Contacto, on_delete=models.SET_NULL, null=True)
    fiscal = models.ForeignKey(Fiscal, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Caja(models.Model):
    clave = models.CharField(max_length=3, null=False, blank=False)
    nombre = models.CharField(max_length=10, null=False, blank=False)

class Departamento(models.Model):
    nombre = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.nombre

class Medida(models.Model):
    nombre = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=10, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    existencia = models.IntegerField(null=False, blank=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    precio = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False, verbose_name='Precio de venta')
    existencia_minima = models.IntegerField(null=False, blank=False, verbose_name='Existencia minima')

class Venta(models.Model):
    fecha = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False)
    total = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)
    vendedor = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    caja = models.ForeignKey(Caja, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    descuento = models.IntegerField(null=True, blank=True)

class MovimentoCaja(models.Model):
    fecha = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    monto_abierto = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Monto de apertura')
    monto_cierre = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Monto de cierre')
    saldo_final = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    movimiento = models.CharField(max_length=1, null=True, blank=True)
    caja = models.ForeignKey(Caja, on_delete=models.SET_NULL, null=True)