from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.


# ADDRESS_CHOICES = (
#     ('B', 'Billing'),
#     ('S', 'Shipping'),
# )


# Start model Address
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    appartment_address = models.CharField(max_length=200)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    # address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    # default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'

# End Model Address
