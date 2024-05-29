from django.contrib import admin
from .models import Registration, Event
from .models import IntroductionImage
from .models import SliderImage

admin.site.register(SliderImage)
admin.site.register(IntroductionImage)
admin.site.register(Registration)
admin.site.register(Event)