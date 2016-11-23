from django import forms
from .models import Venta, Usuario, Articulo



class VentaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Venta
        fields = ( 'usuario', 'articulo')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.


def __init__ (self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

        self.fields["usuario"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

        self.fields["usuario"].help_text = "Seleccione el usuario"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["usuario"].queryset = Usuario.objects.all()

        #En este caso vamos a usar el widget checkbox multiseleccionable.

        #---------------------------------------------------------------

        self.fields["articulo"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

        self.fields["articulo"].help_text = "Seleccione el articulo a comprar"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["articulo"].queryset = Modelo.objects.all()


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('usuario1',)


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('articulo1', 'Precio',)