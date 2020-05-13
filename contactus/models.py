from django.db import models

# Create your models here.

class ContactUsInformation(models.Model):
    head_office = models.CharField(max_length=255)
    mobil = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.head_office


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Contact us'