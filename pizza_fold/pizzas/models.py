from django.db import models


# Create your models here.


class Pizza(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Topping(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
