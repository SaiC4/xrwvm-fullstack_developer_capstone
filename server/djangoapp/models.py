from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    SEDAN = 'SEDAN'
    SUV = 'SUV'
    WAGON = 'WAGON'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        # Add more types as needed
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPES, default=SUV)
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023),
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
