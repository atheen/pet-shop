from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=90)
    age= models.IntegerField()
    available= models.BooleanField(default=True)
    image= models.ImageField()
    price= models.DecimalField(max_digits=10, decimal_places=4)

    def str(self):
        return self.name
