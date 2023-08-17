from django.db import models
class yourModel(models.Model):
    Name=models.CharField(max_length=100)   #it can store string values
    Age=models.IntegerField()  #It can store integer values.
    DOB=models.DateTimeField(auto_now_add=True)  #This means it will automatically set the field to the current date and time when an object is created.
# Create your models here.



class car(models.Model):
    car_name=models.CharField(max_length=20)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.speed
    