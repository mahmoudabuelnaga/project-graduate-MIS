from django.db import models
from django.urls import reverse

# Create your models here.

# Start model Category


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title
# End model Category


# Start model Brand
class Brand(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title
# End model Brand


# Start model Item
class Item(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand, related_name='items', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='products/',
                              default='product_avatar.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    best_seller = models.BooleanField(default=False)
    popular_item = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse(
        #     'products:product_detail',
        #     args=[self.slug]
        # )
        pass

    def get_add_to_cart_url(self):
        # return reverse(
        #     'products:add_to_cart',
        #     args=[self.slug]
        # )
        pass

    def get_remove_from_cart_url(self):
        # return reverse(
        #     'products:remove_from_cart',
        #     args=[self.slug]
        # )
        pass
# End Model Item
