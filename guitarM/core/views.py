from django.shortcuts import render, redirect
from .models import Instrumento
from .forms import InstrumentoForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):

     return render(request, 'core/home.html')

def galeria(request):

     return render(request, 'core/galeria.html')  

def listado_instrumento(request):
    instrumento = Instrumento.objects.all()
    data = {
         'instrumento': instrumento
    }
    return render(request, 'core/listado_instrumentos.html', data) 

@permission_required('core.add_instrumento')
def nuevo_instrumento(request):
     data = {
          'form': InstrumentoForm()
     }

     if request.method == 'POST':
        formulario = InstrumentoForm(request.POST)
        if formulario.is_valid():
             formulario.save()
             data ['mensaje'] = "Guardado correctamente"
        data['form'] = formulario

     return render(request, 'core/nuevo_instrumento.html', data)

def modificar_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id)
    data = {
         'form': InstrumentoForm(instance=instrumento)
    } 

    if request.method == 'POST':
         formulario = InstrumentoForm(data=request.POST, instance=instrumento)
         if formulario.is_valid():
              formulario.save()
              data ['mensaje'] = "Modificado correctamente"
              data ['form'] = formulario

    return render(request, 'core/modificar_instrumento.html', data)


def eliminar_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id) 
    instrumento.delete()

    return redirect(to="listado de instrumentos")



def registro_usuario(request):
     data = {
         'form': CustomUserForm()
    }

     if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
             formulario.save()
             username = formulario.cleaned_data['username']
             password =  formulario.cleaned_data['password1']
             user = authenticate(username=username, password=password)
             login(request, user)
             return redirect(to='home')

     return render(request, 'registration/registrar.html', data)


