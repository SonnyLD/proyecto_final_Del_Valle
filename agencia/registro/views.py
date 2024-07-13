from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.urls import reverse_lazy # type: ignore
from .models import *

from .forms import *

from django.views.generic import ListView # type: ignore
from django.views.generic import CreateView # type: ignore
from django.views.generic import UpdateView # type: ignore
from django.views.generic import DeleteView # type: ignore

from django.contrib.auth import login, authenticate # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth.views import PasswordChangeView # type: ignore

from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore

# Create your views here.
def home(request):
  return render(request, "registro/index.html")

def menu(request):
  return render(request, "registro/menu.html")

def acerca(request):
    return render(request, "registro/acerca.html")

def habitacion(request):
  contexto = {"habitacion": Habitacion.objects.all()}
  return render(request, "registro/habitacion.html", contexto)

#___ Registros

@login_required
def pasajero(request):
  contexto = {"pasajero": Pasajero.objects.all()}
  return render(request, "registro/pasajero.html", contexto)

@login_required
def registro_form(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
        if form.is_valid():
            form.save()  # El método save() está disponible en ModelForm
            return redirect('pasajero')  # Cambia '' por la URL a la que quieras redirigir
    else:
        form = registroForm()
    
    return render(request, "registro/registro_form.html", {"form": form})

@login_required
def registro_update(request, id_registro):
    registro = get_object_or_404(Pasajero, id=id_registro) # type: ignore
    if request.method == "POST":
        form = registroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('pasajero')       
    else:
        form = registroForm(instance=registro)
    
    return render(request, "registro/registro_form.html", {"form": form})

@login_required
def registro_delete(request, id_registro):
    registro = get_object_or_404(Pasajero, id=id_registro) # type: ignore
    registro.delete()
    return redirect('pasajero')


#_____ Hotel

@login_required
def hotel(request):
  contexto = {"hotel": Hotel.objects.all()}
  return render(request, "registro/hotel.html", contexto)

@login_required
def hotelform(request):
    if request.method == 'POST':
        form = hotelForm(request.POST)
        if form.is_valid():
            form.save()  # El método save() está disponible en ModelForm
            return redirect('hotel')  # Cambia '' por la URL a la que quieras redirigir
    else:
        form = hotelForm()
    
    return render(request, "registro/hotelform.html", {"form": form})

@login_required
def hotel_update(request, id_hotel):
    hotel = get_object_or_404(Hotel, id=id_hotel) # type: ignore
    if request.method == "POST":
        form = hotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel')       
    else:
        form = hotelForm(instance=hotel)
    
    return render(request, "registro/hotelform.html", {"form": form})

@login_required
def hotel_delete(request, id_hotel):
    hotel = get_object_or_404(Hotel, id=id_hotel) # type: ignore
    hotel.delete()
    return redirect('hotel')

#______ Pais de Destino
@login_required
def pais_destino_list(request):
    paises = Pais_destino.objects.all()
    return render(request, 'registro/pais_destino_list.html', {'pais_destino': paises})

@login_required
def pais_destino_create(request):
    if request.method == 'POST':
        form = PaisDestinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pais_destino_list')
    else:
        form = PaisDestinoForm()
    return render(request, 'registro/pais_destino_form.html', {'form': form})

@login_required
def pais_destino_update(request, pk):
    pais = get_object_or_404(Pais_destino, pk=pk)
    if request.method == 'POST':
        form = PaisDestinoForm(request.POST, instance=pais)
        if form.is_valid():
            form.save()
            return redirect('pais_destino_list')
    else:
        form = PaisDestinoForm(instance=pais)
    return render(request, 'registro/pais_destino_form.html', {'form': form})

@login_required
def pais_destino_delete(request, pk):
    pais = get_object_or_404(Pais_destino, pk=pk)
    if request.method == 'POST':
        pais.delete()
        return redirect('pais_destino_list')
    return render(request, 'registro/pais_destino_confirm_delete.html', {'object': pais})


#______ Habitaciones
class HabitacionListView(LoginRequiredMixin, ListView):
    model = Habitacion
    template_name = "registro/habitacion_list.html"
    context_object_name = "habitaciones"

class HabitacionCreateView(LoginRequiredMixin, CreateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = "registro/habitacion_form.html"
    success_url = reverse_lazy('habitacion_list')

class HabitacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = "registro/habitacion_form.html"
    success_url = reverse_lazy('habitacion_list')

class HabitacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Habitacion
    template_name = "registro/habitacion_form.html"
    success_url = reverse_lazy('habitacion_list')

#_____ Buscar

@login_required
def buscarPasajeros(request):
    return render(request, "registro/buscar.html")


@login_required
def encontrarPasajeros(request):
    if 'buscar' in request.GET:
        patron = request.GET.get('buscar')
        pasajeros = Pasajero.objects.filter(nombre__icontains=patron)
    else:
        pasajeros = Pasajero.objects.all()

    contexto = {'pasajero': pasajeros}
    return render(request, "registro/pasajero.html", contexto)

# ___ Login / Logout / Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
              # _______ Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except Avatar.DoesNotExist:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            # ______________________________________________________________

            return render(request, "registro/menu.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "registro/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST) # type: ignore
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm() # type: ignore

    return render(request, "registro/registro.html", {"form": miForm})

# ____ Edición de Perfil / Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST, instance=usuario) # type: ignore
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario) # type: ignore
    return render(request, "registro/editarPerfil.html", {"form": miForm})
                                                                                                    
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "registro/cambiarclave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = request.user
            imagen = miForm.cleaned_data["imagen"]
            # Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if avatarViejo.exists():
                avatarViejo.delete()
            # Guardar nuevo avatar
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            # Enviar la imagen al home
            request.session["avatar"] = avatar.imagen.url
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "registro/agregarAvatar.html", {"form": miForm})