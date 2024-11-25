from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def seller_dashboard(request):
    if request.user.user_type!='vendedor':
        return redirect('home')
    productos=Producto.objects.filter(vendedor=request.user)
    return render(request,'vendedor/seller_dashboard.html',{'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form=ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto=form.save(commit=False)
            producto.vendedor = request.user  # Asignar el vendedor actual al producto
            producto.save()
            return redirect('seller_dashboard')
    else:
        form=ProductoForm()
    return render(request, 'vendedor/agregar_producto.html', {'form': form})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, vendedor=request.user)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'dashboard/editar_producto.html', {'form': form})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, vendedor=request.user)
    if request.method == 'POST':
        producto.delete()
        return redirect('seller_dashboard')
    return render(request, 'dashboard/eliminar_producto.html', {'producto': producto})