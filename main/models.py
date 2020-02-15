from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Order(models.Model):
    client = models.CharField(
        max_length=50, 
        validators=[
            RegexValidator(r"[\u0400-\u04FF\s]{3,50}", 
            'Enter the name in cyrillic alphabet or enter from 3 to 50 characters')
        ]
    )
    telephone = models.CharField(
        max_length=17, 
        validators=[
            RegexValidator(r"^(\+380)\(\d{2}\)(\d{3})-(\d{2})-(\d{2})$", 
            'Enter the phone number in the correct format')
        ]
    )
    order_adress = models.CharField(max_length=100)
    destination_adress = models.CharField(max_length=100)
    desired_time = models.DateTimeField()
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    create_datetime = models.DateTimeField(auto_now_add=True)


class Car(models.Model):
    model = models.CharField(max_length=15)
    driver = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def set_available(self):
        self.is_available = True
    
    def set_unavailable(self):
        self.is_available = False

    def __str__(self):
        return '{}'.format(self.model)

