from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.1/ref/models/instances/ # django documentation - models

from django.core.validators import MaxValueValidator, MinValueValidator # for age (minimum 6 and maximum 99)

class Student(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True,unique=True)
    age = models.IntegerField(default=6,validators=[MaxValueValidator(99),MinValueValidator(6)])
    createdTime = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')      # IMAGE upload - Django4Kids, i saved a default placeholder.png in static/image so html always takes a picture withour error

    def __str__(self):
        return f'{self.name}'
    


