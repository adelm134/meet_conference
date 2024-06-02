from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Gallery, SliderImage, IntroductionImage

def index(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    gallery = Gallery.objects.all()
    slider_images = SliderImage.objects.all()
    introduction_images = IntroductionImage.objects.all()
    context = {
        'form': form,
        'gallery': gallery,
        'slider_images': slider_images,
        'introduction_images': introduction_images,
    }
    return render(request, 'index.html', context)