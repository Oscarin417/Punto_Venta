from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
@login_required
def dashboard(request):
    mcaja = MovimentoCaja.objects.all().count()
    ventas = Venta.objects.all().count()
    context = {
        'mcaja': mcaja,
        'ventas': ventas,
    }
    return render(request, 'index.html', context)

def signout(request):
    logout(request)
    return redirect('login')

def sigin(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return redirect('inicio')
    return render(request, 'login.html')

def registro(request):
    e_form = EmployeForm(request.POST or None)
    c_form = ContactoForm(request.POST or None)
    r_form = UserForm(request.POST or None)
    context = {
        'e_form': e_form,
        'c_form': c_form,
        'r_form': r_form,
    }

    if request.method == 'POST':
        try:
            if e_form.is_valid() and c_form.is_valid() and r_form.is_valid():
                e = e_form.save(commit=False)
                c = c_form.save()
                r = r_form.save()
                e.contacto = c
                e.usuario = r
                e.save()
                login(request, r)
                return redirect('inicio')
            else:
                print(e_form.errors)
                print(c_form.errors)
                print(r_form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'registro.html', context)

@login_required
def negocio(request):
    negocios = Negocio.objects.all()

    context = {'negocios': negocios}

    return render(request, 'negocio/list.html', context)

@login_required
def negocio_crear(request):
    n_form = NegocioForm(request.POST or None)
    c_form = ContactoForm(request.POST or None)
    d_form = DomicilioForm(request.POST or None)
    f_form = FiscalForm(request.POST or None)

    context = {
        'n_form': n_form,
        'c_form': c_form,
        'd_form': d_form,
        'f_form': f_form
    }

    if request.method == 'POST':
        try:
            if n_form.is_valid() and c_form.is_valid() and d_form.is_valid() and f_form.is_valid():
                n = n_form.save(commit=False)
                f = f_form.save(commit=False)
                d = d_form.save()
                c = c_form.save()
                f.domicilio = d
                f.save()
                n.contacto = c
                n.fiscal = f
                n.save()
                return redirect('negocio')
            else:
                print(n_form.errors)
                print(c_form.errors)
                print(d_form.errors)
                print(f_form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'negocio/create.html', context)

@login_required
def negocio_editar(request, pk):
    negocio = Negocio.objects.get(pk=pk)
    contacto = negocio.contacto
    fiscal = negocio.fiscal
    domicilio = negocio.fiscal.domicilio
    n_form = NegocioForm(request.POST or None, instance=negocio)
    c_form = ContactoForm(request.POST or None, instance=contacto)
    d_form = DomicilioForm(request.POST or None, instance=domicilio)
    f_form = FiscalForm(request.POST or None, instance=fiscal)

    context = {
        'n_form': n_form,
        'c_form': c_form,
        'd_form': d_form,
        'f_form': f_form
    }

    if request.method == 'POST':
        try:
            if n_form.is_valid() and c_form.is_valid() and d_form.is_valid() and f_form.is_valid():
                d_form.save()
                f_form.save()
                c_form.save()
                n_form.save()
                return redirect('negocio')
            else:
                print(n_form.errors)
                print(c_form.errors)
                print(d_form.errors)
                print(f_form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'negocio/edit.html', context)

@login_required
def negocio_eliminar(request, pk):
    negocio = Negocio.objects.get(pk=pk)
    contacto = negocio.contacto
    fiscal = negocio.fiscal
    domicilio = negocio.fiscal.domicilio

    if request.method == 'POST':
        domicilio.delete()
        fiscal.delete()
        contacto.delete()
        negocio.delete()
        return redirect('negocio')

@login_required    
def marca(request):
    marcas = Marca.objects.all()
    context = {'marcas': marcas}

    return render(request, 'marca/list.html', context)

@login_required
def marca_crear(request):
    form = MarcaForm(request.POST or None)
    context = {'form':form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('marca')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'marca/create.html', context)

@login_required
def marca_editar(request, pk):
    marca = Marca.objects.get(pk=pk)
    form = MarcaForm(request.POST or None, instance=marca)
    context = {
        'form': form
    }

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('marca')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'marca/edit.html', context)

@login_required
def marca_eliminar(request, pk):
    marca = Marca.objects.get(pk=pk)

    if request.method == 'POST':
        marca.delete()
        return redirect('marca')

@login_required    
def cliente(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}

    return render(request, 'cliente/list.html', context)

@login_required
def cliente_crear(request):
    c_form = ClienteForm(request.POST or None)
    con_form = ContactoForm(request.POST or None)
    f_form = FiscalForm(request.POST or None)
    d_form = DomicilioForm(request.POST or None)
    context = {
        'c_form': c_form,
        'con_form': con_form,
        'f_form': f_form,
        'd_form': d_form
    }

    if request.method == 'POST':
        try:
            if c_form.is_valid() and con_form.is_valid() and f_form.is_valid() and d_form.is_valid():
                cli = c_form.save(commit=False)
                f = f_form.save(commit=False)
                d = d_form.save()
                f.domicilio = d
                f.save()
                con = con_form.save()
                cli.contacto = con
                cli.fiscal = f
                cli.save()
                return redirect('cliente')
            else:
                print(c_form.errors)
                print(con_form.errors)
                print(f_form.errors)
                print(d_form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'cliente/create.html', context)

@login_required
def cliente_editar(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    contacto = cliente.contacto
    fiscal = cliente.fiscal
    domiclio = cliente.fiscal.domicilio
    c_form = ClienteForm(request.POST or None, instance=cliente)
    con_form = ContactoForm(request.POST or None, instance=contacto)
    f_form = FiscalForm(request.POST or None, instance=fiscal)
    d_form = DomicilioForm(request.POST or None, instance=domiclio)
    context = {
        'c_form': c_form,
        'con_form': con_form,
        'f_form': f_form,
        'd_form': d_form
    }

    if request.method == 'POST':
        try:
            if c_form.is_valid() and con_form.is_valid() and f_form.is_valid() and d_form.is_valid():
                con_form.save()
                d_form.save()
                f_form.save()
                c_form.save()
                return redirect('cliente')
            else:
                print(c_form.errors)
                print(con_form.errors)
                print(f_form.errors)
                print(d_form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'cliente/edit.html', context)

@login_required
def cliente_eliminar(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    contacto = cliente.contacto
    fiscal = cliente.fiscal
    domiclio = cliente.fiscal.domicilio

    if request.method == 'POST':
        contacto.delete()
        domiclio.delete()
        fiscal.delete()
        cliente.delete()
        return redirect('cliente')

@login_required    
def caja(request):
    cajas = Caja.objects.all()
    empleado = Empleado.objects.get(usuario=request.user)
    context = {
        'cajas':cajas,
        'empleado': empleado
        }

    return render(request, 'caja/list.html', context)

@login_required
def caja_agregar(request):
    form = CajaForm(request.POST or None)
    context = {'form':form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('caja')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'caja/create.html', context)

@login_required
def caja_editar(request, pk):
    caja = Caja.objects.get(pk=pk)
    form = CajaForm(request.POST or None, instance=caja)
    context = {'form':form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('caja')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'caja/edit.html', context)

@login_required
def caja_eliminar(request, pk):
    caja = Caja.objects.get(pk=pk)

    if request.method == 'POST':
        caja.delete()
        return redirect('caja')

@login_required    
def departamento(request):
    departamantos = Departamento.objects.all()
    context = {'departamentos': departamantos}

    return render(request, 'departamento/list.html', context)

@login_required
def departamento_crear(request):
    form = DepartamanetoForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('departamento')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'departamento/create.html', context)

@login_required
def departamento_editar(request, pk):
    departamento = Departamento.objects.get(pk=pk)
    form = DepartamanetoForm(request.POST or None, instance=departamento)
    context = {'form': form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('departamento')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'departamento/edit.html', context)

@login_required
def departamento_eliminar(request, pk):
    departamento = Departamento.objects.get(pk=pk)

    if request.method == 'POST':
        departamento.delete()
        return redirect('departamento')

@login_required    
def medida(request):
    medidas = Medida.objects.all()
    context = {'medidas': medidas}

    return render(request, 'medida/list.html', context)

@login_required
def medida_crear(request):
    form = MedidaForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('medida')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'medida/create.html', context)

@login_required
def medida_editar(request, pk):
    medida = Medida.objects.get(pk=pk)
    form = MedidaForm(request.POST or None, instance=medida)
    context = {'form': form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('medida')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'medida/edit.html', context)

@login_required
def medida_eliminar(request, pk):
    medida = Medida.objects.get(pk=pk)

    if request.method == 'POST':
        medida.delete()
        return redirect('medida')

@login_required    
def producto(request):
    productos = Producto.objects.all()
    context = {'productos': productos}

    return render(request, 'producto/list.html', context)

@login_required
def producto_crear(request):
    form = ProductoForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('producto')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'producto/create.html', context)

@login_required
def producto_editar(request, pk):
    producto = Producto.objects.get(pk=pk)
    form = ProductoForm(request.POST or None, instance=producto)
    context = {'form': form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('producto')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'producto/edit.html', context)

@login_required
def producto_eliminar(request, pk):
    producto = Producto.objects.get(pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('producto')

@login_required   
def empleado(request):
    empleados = Empleado.objects.all()
    context = {'empleados': empleados}

    return render(request, 'empleado/list.html', context)

@login_required
def empleado_crear(request):
    e_form = EmpleadoForm(request.POST or None)
    u_form = UserForm(request.POST or None)
    c_form = ContactoForm(request.POST or None)
    context = {
        'e_form': e_form,
        'u_form': u_form,
        'c_form': c_form
    }

    if request.method == 'POST':
        try:
            if e_form.is_valid() and u_form.is_valid() and c_form.is_valid():
                e = e_form.save(commit=False)
                u = u_form.save()
                c = c_form.save()
                e.usuario = u
                e.contacto = c
                e.save()
                return redirect('empleado')
            else:
                print(e_form.errors)
                print(u_form.errors)
                print(c_form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'empleado/create.html', context)

@login_required
def empleado_editar(request, pk):
    empleado = Empleado.objects.get(pk=pk)
    usuario = empleado.usuario
    contacto = empleado.contacto
    e_form = EmpleadoForm(request.POST or None, instance=empleado)
    u_form = UserForm(request.POST or None, instance=usuario)
    c_form = ContactoForm(request.POST or None, instance=contacto)
    context = {
        'e_form': e_form,
        'u_form': u_form,
        'c_form': c_form
    }

    if request.method == 'POST':
        try:
            if e_form.is_valid() and u_form.is_valid() and c_form.is_valid():
                u_form.save()
                c_form.save()
                e_form.save()
                return redirect('empleado')
            else:
                print(e_form.errors)
                print(u_form.errors)
                print(c_form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'empleado/edit.html', context)

@login_required
def empleado_eliminar(request, pk):
    empleado = Empleado.objects.get(pk=pk)
    usuario = empleado.usuario
    contacto = empleado.contacto

    if request.method == 'POST':
        contacto.delete()
        usuario.delete()
        empleado.delete()
        return redirect('empleado')
    
@login_required
def abrir_caja(request, pk):
    caja = Caja.objects.get(pk=pk)
    empleado = Empleado.objects.get(usuario=request.user)
    form = MCajaForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                f = form.save(commit=False)
                f.caja = caja
                f.empleado = empleado
                f.fecha = datetime.now()
                f.movimiento = 'A'
                request.session['estado'] = 1
                request.session['caja'] = caja.id
                f.save()
                return redirect('caja')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'caja/abrir.html', context)

@login_required
def cerrar_caja(request, pk):
    caja = Caja.objects.get(pk=pk)
    caja_abierta = MovimentoCaja.objects.get(caja=caja, movimiento='A')
    empleado = Empleado.objects.get(usuario=request.user)
    form = MCajaForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        try:
            if form.is_valid():
                f = form.save(commit=False)
                f.caja = caja
                f.empleado = empleado
                f.fecha = datetime.now()
                f.movimiento = 'E'
                f.monto_abierto = caja_abierta.monto_abierto
                f.saldo_final = f.monto_cierre - f.monto_abierto
                request.session['estado'] = 0
                request.session['caja'] = caja.id
                f.save()
                return redirect('caja')
            else:
                print(form.errors)
        except Exception as e:
            print(f'error: {e}')

    return render(request, 'caja/cerrar.html', context)

@login_required
def venta(request):
    ventas = Venta.objects.all()
    context = {'ventas': ventas}

    return render(request, 'venta/list.html', context)

def autocomplete_producto(request):
    if "term" in request.GET:
        qs = Producto.objects.filter(nombre__icontains=request.GET.get("term"))
        titles = list()
        for p in qs:
            datos = {
                'id': p.id,
                'label': p.nombre,
                'precio': p.precio,
                'existencia': p.existencia
            }
            titles.append(datos)
        return JsonResponse(titles, safe=False)