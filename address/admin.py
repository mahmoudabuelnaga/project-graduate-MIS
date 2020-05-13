from django.contrib import admin
from .models import Address

# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'apartment_address',
                    'country', 'zip', 'address_type', 'default']
    list_filter = ['address_type', 'default', 'country']
    search_fields = ('user__username', 'street_address',
                     'apartment_address', 'country', 'zip')
