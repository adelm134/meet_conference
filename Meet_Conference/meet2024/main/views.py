from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Gallery, SliderImage, IntroductionImage
from django.contrib import messages

def index(request):
    return render_index(request, 'index.html')

def index_en(request):
    return render_index(request, 'english.html', lang='en')

def render_index(request, template_name, lang='ru'):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            if lang == 'en':
                return redirect('index_en')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')

    gallery = Gallery.objects.all()
    slider_images = SliderImage.objects.all()
    introduction_images = IntroductionImage.objects.all()
    context = {
        'form': form,
        'gallery': gallery,
        'slider_images': slider_images,
        'introduction_images': introduction_images,
    }
    return render(request, template_name, context)