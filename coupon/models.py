from django.db import models

# Create your models here.


# Start model Coupon
class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.code
# End Model Coupon
