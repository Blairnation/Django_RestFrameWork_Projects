from typing import Any
from django.db import models

# Create your models here.
class CarPlan(models.Model):
    plan_name = models.CharField(max_length=20)
    years_of_warranty = models.PositiveIntegerField(default=1)
    finance_plan = models.CharField(max_length=20, default='unavailable')

    def __str__(self) -> str:
        return self.plan_name


class Car(models.Model):
    car_plan = models.ForeignKey(CarPlan, on_delete=models.SET_NULL, null=True)
    brand = models.CharField(max_length=250)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return self.brand
    
    
class PostRates(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)

    # def __str__(self) -> str:
    #     return self.likes

class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField(max_length=200)
    rates = models.OneToOneField(PostRates, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.post_title


class Modules(models.Model):
    module_name = models.CharField(max_length=50)
    module_duration = models.IntegerField()
    classroom = models.IntegerField()

    def __str__(self) -> str:
        return self.module_name

class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(Modules)

    def __str__(self) -> str:
        return self.name 
    
class Forecast(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f'{self.timestamp}'    