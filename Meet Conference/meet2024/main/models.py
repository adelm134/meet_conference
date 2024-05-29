from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class IntroductionImage(models.Model):
    image = models.ImageField(upload_to='introduction/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption if self.caption else "Introduction Image"
    
class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption if self.caption else "Slider Image"