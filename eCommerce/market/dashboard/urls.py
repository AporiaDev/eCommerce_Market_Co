from django.urls import path
from .views import seller_dashboard, agregar_producto, editar_producto, eliminar_producto,cerrar_sesion

urlpatterns = [path('seller/',seller_dashboard,name='seller_dashboard'),
    path('seller/add/',agregar_producto,name='agregar_producto'),
    path('seller/edit/<int:producto_id>/',editar_producto, name='editar_producto'),
    path('seller/delete/<int:producto_id>/',eliminar_producto, name='eliminar_producto'),
    path('seller/logout/',cerrar_sesion,name='cerrar_sesion')
]