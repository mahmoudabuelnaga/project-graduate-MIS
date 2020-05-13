from django.contrib import admin
from .models import ContactUsInformation, ContactUs

# Register your models here.
admin.site.register(ContactUsInformation)
admin.site.register(ContactUs)