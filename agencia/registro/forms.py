from django import forms # type: ignore
from .models import Pasajero, Hotel, Habitacion, Pais_destino
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # type: ignore
from .models import Avatar

class registroForm(forms.ModelForm):
    class Meta:
        model =  Pasajero   # type: ignore
        fields = ['nombre', 'apellido', 'email', 'sexo']

class hotelForm(forms.ModelForm):
    class Meta:
        model =  Hotel   # type: ignore
        fields = ['nombre','CheckIn', 'CheckOut', 'numeroNoches']
        widgets = {
            'CheckIn': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'CheckOut': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero', 'doble', 'simple']      


class PaisDestinoForm(forms.ModelForm):
    class Meta:
        model = Pais_destino
        fields = ['nombre', 'fechaLLegada'] # Agrega los campos que necesites         


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']        

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']        