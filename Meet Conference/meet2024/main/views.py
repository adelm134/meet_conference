from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Gallery

def index(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    gallery = Gallery.objects.all()
    context = {
        'form': form,
        'gallery': gallery,
    }
    return render(request, 'index.html', context)