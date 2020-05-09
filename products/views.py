from django.shortcuts import render, get_object_or_404
from .models import Item, Category, Brand
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    item_3 = Item.objects.all()[:3]
    pop_items = Item.objects.filter(popular_item=True)[:8]
    best_item = Item.objects.filter(best_seller=True)[:8]

    context = {
        'item_3': item_3,
        'pop_items': pop_items,
        'best_item': best_item,
    }
    return render(request, 'index.html', context)


def product_list_by_category(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Item.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # paginator
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(10)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'product_list_by_category.html', context)


def product_list_by_brand(request, brand_slug=None):
    brand = None
    brands = Brand.objects.all()
    products = Item.objects.all()

    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)

    # paginator
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'brand': brand,
        'brands': brands,
        'products': products,
    }
    return render(request, 'product_list_by_brand.html', context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product_detail.html'
    context_object_name = 'item'
