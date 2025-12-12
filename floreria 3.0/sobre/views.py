from django.shortcuts import render, redirect
from .forms import AboutForm
from django.contrib import messages

def formulario_sobre(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensaje enviado. Gracias.")
            return redirect('sobre:sobre')
    else:
        form = AboutForm()
    return render(request, 'sobre/sobre.html', {'form': form})