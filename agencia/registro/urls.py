from django.urls import path, include # type: ignore
from registro.views import *
from . import views

from django.contrib.auth.views import LogoutView # type: ignore

urlpatterns = [
    path('', home, name = "home"),
    path('menu/', menu, name = "menu"),
    path('acerca/', acerca, name="acerca"),
    path('habitacion/', habitacion, name = "habitacion"),
    path('pais_destino/', pais_destino_list, name = "pais_destino"),

    #___ Registro
    path('pasajero/', pasajero, name = "pasajero"),
    path('registro_form/', registro_form, name="registro_form"),
    path('registro_update/<id_registro>/', registro_update, name="registro_update"),
    path('registro_delete/<id_registro>/', registro_delete, name="registro_delete"),

    #___ Hotel
    path('hotel/', hotel, name = "hotel"),
    path('hotelform/', hotelform, name="hotelform"),
    path('hotel_update/<int:id_hotel>/', hotel_update, name="hotel_update"),
    path('hotel_delete/<int:id_hotel>/', hotel_delete, name='hotel_delete'),

    #___ Habitacion
    path('habitacion/', HabitacionListView.as_view(), name='habitacion_list'),
    path('habitacion/nueva/', HabitacionCreateView.as_view(), name='habitacion_create'),
    path('habitacion/editar/<int:pk>/', HabitacionUpdateView.as_view(), name='habitacion_update'),
    path('habitacion/eliminar/<int:pk>/', HabitacionDeleteView.as_view(), name='habitacion_delete'),
    
    #___ Pais de destino
    path('pais_destino/', views.pais_destino_list, name='pais_destino_list'),
    path('pais_destino/new/', views.pais_destino_create, name='pais_destino_create'),
    path('pais_destino/<int:pk>/edit/', views.pais_destino_update, name='pais_destino_update'),
    path('pais_destino/<int:pk>/delete/', views.pais_destino_delete, name='pais_destino_delete'),

    #____ Buscar
    path('buscarPasajeros/', buscarPasajeros, name="buscarPasajeros"),
    path('encontrarPasajeros/', encontrarPasajeros, name="encontrarPasajeros"),


    #___ Login / Logout / Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registro/', register, name="registro"),

    
    #___ Edición de Perfil / Avatar
    path('edit_profile/', views.editProfile, name='editProfile'),
    path('<int:pk>/password/', views.CambiarClave.as_view(), name='cambiarClave'),
    path('agregar_avatar/', views.agregarAvatar, name='agregarAvatar'),
]
