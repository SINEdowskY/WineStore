from django.db import models
from datetime import date, timedelta, datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class Wine(models.Model):
    class WineType(models.TextChoices):
        RED = "red", "Red"
        WHITE = "white", "White"
        ROSE = "rose", "Rose"
        SPARK = "sparkling", "Sparkling"
       
    class FoodMatching(models.TextChoices):
        CHICKEN_TURKEY ="Chicken and Turkey"
        DUCK_GOOSE = "Duck and Goose"
        PORK = "Pork"
        LAMB = "Lamb"
        BEEF_N_VENISON = "Beef and Venison"
        GREEN_VEG = "Green Vegetables"
        ROOT_VEG = "Root Vegetables"
        MUSHROOM ="Mushroom"
        TOMATO = "Tomato-based"
        SPICY = "Spicy"
        WHITE_FISH = "White Fish"
        MEATY_OILY_FISH = "Meaty and Oily Fish"
        SHELLFISH = "Shellfish, Crab and Lobster"
        GCHEESE_FETA = "Goats' Cheese and Feta"
        MANCHEGO_PARMESAN = "Manchego and Parmesan"
        CHEDDAR_GRUYERE = "Cheddar and Gruyere"
        BLUE_CHEESE = "Blue Cheese"
        BRIE_CAMEMBERT = "Brie and Camembert"
        FRUIT_BASED = "Fruit-based Desserts"
        CHOCO_CARAMEL = "Chocolate and Caramel"
        CAKE_CREAM = "Cakes and Cream"
    
    title = models.CharField(max_length=40)
    type = models.CharField(
        max_length=10,
        choices=WineType.choices
    )
    price = models.DecimalField(decimal_places=2, max_digits=12)
    grape_type = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    pairs_well = models.CharField(
        max_length=30,
        choices=FoodMatching.choices
    )
    origin_country = models.CharField(max_length=20, default="France")
    storage_amount = models.IntegerField()

    def __str__(self):
        return self.title

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(
        validators=[
            MaxValueValidator(limit_value=date.today() - timedelta(days=365*18))
        ]
        )
    address_street = models.CharField(max_length=50)
    address_number = models.CharField(max_length=3)
    address_apartament_number = models.CharField(max_length=3, blank=True)
    zip_code = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                regex=r"^\d{2}-\d{3}$",
                message="give valid postal code in format: XX-XXX"
            )
        ]
    )
    address_city = models.CharField(max_length=50, default="Rzeszów")
    phone_number = models.CharField(max_length=9)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        verbose = f"{self.first_name} {self.last_name} {self.address_street} {self.address_number}, {self.address_city}"
        return verbose

class Cart(models.Model):
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    wine_id = models.ForeignKey(Wine, on_delete=models.CASCADE)
    amount = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(limit_value=1)
        ]
    )


class Order(models.Model):
    class Shipment(models.TextChoices):
        INPOST = "InPost"
        POST = "Poczta Polska"
        DHL = "DHL"

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    order_value = models.DecimalField(decimal_places=2, max_digits=12)
    order_set_date = models.DateTimeField(default=datetime.now())
    is_recived = models.BooleanField(default=False)
    wines = models.ManyToManyField(Wine)
    shipment = models.CharField(
        max_length=20,
        choices=Shipment.choices,
        default=Shipment.INPOST
    )
