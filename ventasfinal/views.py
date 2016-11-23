from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .forms import VentaForm, UsuarioForm, ArticuloForm
from ventasfinal.models import Venta, Usuario, Articulo
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required





def venta_nuevo(request):
    if request.method == "POST":
        formulario = VentaForm(request.POST,request.FILES)
        if formulario.is_valid():

            for usuario_id in request.POST.getlist('usuario'):
                for articulo_id in request.POST.getlist('articulo'):
                    fecha = timezone.now()         
                    venta = Venta(fecha_ingreso=fecha,usuario_id=usuario_id,articulo_id=articulo_id)
                    formulario.save()
                    return redirect('ventasfinal.views.venta_lista')
                    messages.add_message(request, messages.SUCCESS, 'Venta Guardada Exitosamente')

    else:
        formulario = VentaForm()
    return render(request, 'ventasfinal/venta_nuevo.html', {'formulario': formulario})


@login_required

def venta_lista(request):
    ventas = Venta.objects.filter(fecha_ingreso=timezone.now()).order_by('fecha_ingreso')
    return render(request, 'ventasfinal/venta_lista.html', {'ventas':ventas})

def venta_detalle(request, pk):
    post = get_object_or_404(Venta, pk=pk)
    return render(request, 'ventasfinal/venta_detalle.html', {'post':post})

def venta_editar(request, pk):
    ventas = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        formulario = VentaForm(request.POST,request.FILES, instance=ventas)
        if formulario.is_valid():
            for usuario_id in request.POST.getlist('usuario'):
                for articulo_id in request.POST.getlist('articulo'):
                    fecha = timezone.now()
                    venta = Venta(fecha_ingreso=fecha,usuario_id=usuario_id,articulo_id=articulo_id)
                    formulario.save()
                    #return render(request, 'ventasfinal/venta_lista.html', {'ventass':ventas})
                    return redirect('ventasfinal/venta_lista.html', pk=venta.pk)
                    messages.add_message(request, messages.SUCCESS, 'Venta Guardada Exitosamente')

    else:
        formulario = VentaForm(instance=ventas)
    return render(request, 'ventasfinal/venta_editar.html', {'formulario': formulario})
    


def vehiculo_eliminar(request, pk):
    post = get_object_or_404(Venta, pk=pk)
    post.delete()
    return redirect('ventasfinal/venta_lista.html', pk=venta.pk)


def usuario_nueva(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            usuario.save()
            return redirect('ventasfinal.views.usuario_lista')
    else:
        formulario = UsuarioForm()
    return render(request, 'ventasfinal/usuario_nueva.html', {'formulario': formulario})

def usuario_lista(request):
    usuario = usuario.objects.all 
    return render(request, 'ventasfinal/usuario_lista.html', {'usuario':usuario})

def usuario_detalle(request, pk):
    post = get_object_or_404(Marca, pk=pk)
    return render(request, 'ventasfinal/usuario_detalle.html', {'post':post})

def usuario_editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            usuario.save()
            return redirect('ventasfinal.views.usuario_detalle', pk=usuario.pk)
    else:
        formulario = UsuarioForm()
    return render(request, 'ventasfinal/usuario_editar.html', {'formulario': formulario})
    
    


def usuario_eliminar(request, pk):
    post = get_object_or_404(Usuario, pk=pk)
    post.delete()
    return redirect('ventasfinal/usuario_lista.html', pk=post.pk)





def articulo_nuevo(request):
    if request.method == "POST":
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            modelo = formulario.save(commit=False)
            modelo.save()
            return redirect('ventasfinal.views.articulo_lista')
    else:
        formulario = ArticuloForm()
    return render(request, 'ventasfinal/articulo_nuevo.html', {'formulario': formulario})

def articulo_lista(request):
    articulo = Articulo.objects.all 
    return render(request, 'ventasfinal/articulo_lista.html', {'articulo':articulo})

def articulo_detalle(request, pk):
    post = get_object_or_404(Articulo, pk=pk)
    return render(request, 'ventasfinal/articulo_detalle.html', {'post':post})

def articulo_editar(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == "POST":
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            articulo = formulario.save(commit=False)
            articulo.save()
            return redirect('ventasfinal.views.articulo_detalle', pk=articulo.pk)
    else:
        formulario = ArticuloForm()
    return render(request, 'ventasfinal/articulo_editar.html', {'formulario': formulario})
    
    


def articulo_eliminar(request, pk):
    post = get_object_or_404(Articulo, pk=pk)
    post.delete()
    return redirect('ventasfinal/articulo_lista.html', pk=post.pk)

    