from django.db import models
from django.urls import reverse
from django.db.models import Q

# Create your models here.

# Start model Category


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.title
# End model Category


# Start model Brand
class Brand(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse('products:product_list_by_brand', args=[self.slug])

    def __str__(self):
        return self.title
# End model Brand


# Start model Item

class ItemQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(category__title__icontains=query) |
                   Q(brand__title__icontains=query)
                   )
        return self.filter(lookups).distinct()


class ItemManager(models.Manager):
    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class Item(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand, related_name='items', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='products/',
                              default='product_avatar.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    best_seller = models.BooleanField(default=False)
    popular_item = models.BooleanField(default=False)

    objects = ItemManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'products:product_detail',
            args=[self.pk, self.slug]
        )

    def get_add_to_cart_url(self):
        return reverse(
            'orders:add_to_cart',
            args=[self.slug]
        )

    def get_remove_from_cart_url(self):
        return reverse(
            'orders:remove_from_cart',
            args=[self.slug]
        )
# End Model Item
