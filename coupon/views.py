from django.shortcuts import render, get_object_or_404
from .models import Coupon
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from .forms import CouponForm
from orders.models import Order, OrderItem
# Create your views here.


def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon

    except ObjectDoesNotExist:
        messages.warning(self.request, "This coupon does not exist.")
        return redirect('address:checkout')


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect('address:checkout')

            except ObjectDoesNotExist:
                messages.warning(
                    self.request, "You do not have an active order")
                return redirect('address:checkout')
