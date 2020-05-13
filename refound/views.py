from django.shortcuts import render, redirect
from .forms import RefoundForm
from django.views.generic import View
from .models import Refund
from django.core.exceptions import ObjectDoesNotExist
from orders.models import Order
from .models import Refund
from django.contrib import messages
# Create your views here.


class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefoundForm()
        context = {
            'form': form,
        }
        return render(self.request, 'request_refund.html', context)

    def post(self, *args, **kwargs):
        form = RefoundForm(self.request.POST)
        if form.is_valid():
            ref_code = form.cleaned_data.get('ref_code')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')

            try:
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                refound = Refund()
                refound.order = order
                refound.reason = message
                refound.email = email
                refound.save()

                messages.info(self.request, "Your request was received.")
                return redirect("refounds:request-refound")

            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist.")
                return redirect("refounds:request-refound")
