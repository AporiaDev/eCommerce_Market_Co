from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from users.models import User
from .forms import ProductoForm
from django.contrib.auth import logout

def seller_dashboard(request):
    if request.user.user_type!='vendedor':
        return redirect('home')
    productos=Producto.objects.filter(vendedor=request.user)
    context={'productos':productos,'username':request.user.first_name+' '+request.user.last_name}
    return render(request,'vendedor/seller_dashboard.html',context)

def agregar_producto(request):
    if request.method == 'POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            producto=form.save(commit=False)
            producto.vendedor=request.user  #Asignar el vendedor actual al producto
            producto.save()
            return redirect('seller_dashboard')
    else:
        form=ProductoForm()
    return render(request,'vendedor/agregar.html',{'form':form})


def editar_producto(request,producto_id):
    producto=get_object_or_404(Producto,id=producto_id,vendedor=request.user)
    if request.method=='POST':
        form = ProductoForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = ProductoForm(instance=producto)
    return render(request,'vendedor/editar.html',{'form': form,'producto':producto})


def eliminar_producto(request, producto_id):
    producto=get_object_or_404(Producto, id=producto_id, vendedor=request.user)
    if request.method=='POST':
        producto.delete()
        return redirect('seller_dashboard')
    return render(request, 'vendedor/eliminar.html',{'producto':producto})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def cliente_dashboard(request):
    if request.user.user_type != 'cliente':
        return redirect('home')
    productos_sale=Producto.objects.filter(stock__gt=0)
    producto_vendedor=[]
    for producto in productos_sale:
        vendedor = User.objects.get(id=producto.vendedor_id)
        producto_vendedor.append({'producto':producto,'vendedor_nombre':vendedor.first_name+' ' +vendedor.last_name})
    context = {'producto_vendedor':producto_vendedor,'username':request.user.first_name+ ' ' +request.user.last_name}
    return render(request, 'cliente/cliente_dashboard.html',context)

def pasarela_pago(request,producto_id):
    producto=get_object_or_404(Producto,id=producto_id)
    producto.stock-=1
    producto.save()
    context={'producto':producto}
    return render(request,'cliente/pasarela_pago.html',context)

def abortar_comprar(request,producto_id):
    producto=get_object_or_404(Producto,id=producto_id)
    producto.stock+=1
    producto.save()
    return redirect('cliente_dashboard')