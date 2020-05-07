from django.db import models
from django.contrib.auth.models import User
from products.models import Item
from address.models import Address
from payments.models import Payment
from coupon.models import Coupon
# Create your models here.

# Start model OrderItem


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

    def get_total_item_price(self):
        return self.quantity * self.item.price

# End Model OrderItem


# Start model Order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_address = models.ForeignKey(Address,
                                         related_name='shipping_address',
                                         on_delete=models.SET_NULL,
                                         null=True, blank=True)
    billing_address = models.ForeignKey(Address,
                                        related_name='billing_address',
                                        on_delete=models.SET_NULL,
                                        null=True, blank=True)
    payment = models.ForeignKey(Payment,
                                on_delete=models.SET_NULL,
                                blank=True, null=True)
    coupon = models.ForeignKey(Coupon,
                               on_delete=models.SET_NULL,
                               blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += self.items.get_total_item_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

# End Model Order
