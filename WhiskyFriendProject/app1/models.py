from django.db import models
from django.contrib.auth.models import User

# Create your models here.


BOTTLES = (
    (1, 200),
    (2, 500),
    (3, 700),
    (4, 750),
    (5, 1000),
)

ORDERS = (
    (1, 50),
    (2, 100),
    (3, 200)
)


class Spirit(models.Model):
    name = models.CharField(max_length=64, verbose_name="nazwa")
    country = models.CharField(max_length=64, verbose_name="kraj")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="cena")
    capacity = models.IntegerField(choices=BOTTLES, verbose_name="pojemnosc")
    picture = models.ImageField(upload_to="static/images", blank=True, null=True)

    def __str__(self):
        return " ".join([self.name])

    @property
    def reserved(self):
        # import pdb; pdb.set_trace()
        available_quantity = self.get_capacity_display()
        all_orders = Order.objects.filter(spirit_id=self.id)
        for order in all_orders:
            if available_quantity > 0 and order.get_quantity_display() < available_quantity:
                available_quantity -= order.get_quantity_display()
        return available_quantity

    def sample_price(self, quantity):
        bottle_price = self.price
        bottle_capacity = self.get_capacity_display()
        ml_price = bottle_price / bottle_capacity
        return round(quantity * ml_price)

    @property
    def price200(self):
        return self.sample_price(200)

    @property
    def price100(self):
        return self.sample_price(100)

    @property
    def price50(self):
        return self.sample_price(50)


class Order(models.Model):
    spirit = models.ForeignKey(Spirit, verbose_name="przedmiot")
    quantity = models.IntegerField(choices=ORDERS)
    user = models.ForeignKey(User)


class Slainteet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.content
