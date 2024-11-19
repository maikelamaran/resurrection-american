from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def register_view(request):
    if request.method == "POST":#el form ha sido submited
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            login(request,form.save())#aprovecho y logueo el usuario ademas de salvar, form.save() retorna un usuario
            if "next" in request.POST:#quiero que si hay next vaya a donde quiera que next me diga para ir
                return redirect(request.POST.get('next'))
            return redirect("cars:list")#aqui si el form is valid y todo salió bien
    else:#caso get request, simplemente envio el formulario vacio
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})#form no es válido  o caso get request


def login_view(request):  # Cambiamos el nombre de la función aquí
    if request.method == "POST":  # el form ha sido submited
        form = AuthenticationForm(data=request.POST)  # authenticationform espera que le pases el argument data
        if form.is_valid():            
            login(request, form.get_user())  # usamos el login renombrado
            if 'next' in request.POST:#quiero que si hay next vaya a donde quiera que next me diga para ir
                return redirect(request.POST.get('next'))
            return redirect("cars:list")  # aqui si el form is valid y todo salió bien      
            
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})  # form no es válido o caso get request

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("cars:list")