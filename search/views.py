from django.shortcuts import render
from django.db.models import Q
from products.models import Item
from django.views.generic import ListView

# Create your views here.


class SearchItemView(ListView):
    template_name = 'search_product_list.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(SearchItemView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            return Item.objects.search(query)
        return Item.objects.all()
