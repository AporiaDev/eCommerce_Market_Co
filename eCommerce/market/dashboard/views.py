from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

def seller_dashboard(request):
    if request.user.role != 'vendedor':
        return redirect('home')
    productos = Producto.objects.filter(vendedor=request.user)
    return render(request,'dashboard/seller_dashboard.html',{'productos': productos})
