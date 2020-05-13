from orders.views import create_ref_code
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Payment
from django.views.generic import View, ListView, DetailView
from address.forms import CheckoutForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from orders.models import Order, OrderItem
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.


class PaymentView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if order.billing_address:
                context = {
                    'order': order,
                    'DISPLAY_COUPON_FORM': False
                }
                return render(self.request, 'payment.html', context)
            else:
                messages.warning(self.request, "You have not added a address")
                return redirect("address:checkout")
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order.")
            return redirect("/")

    def post(self, *args, **Kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        amount = int(order.get_total() * 100)  # cents
        token = self.request.POST.get('stripeToken')

        try:
            # Use Stripe's library to make requests...
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                source=token
            )

            # Create the Payment
            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user = self.request.user
            payment.amount = order.get_total()
            payment.save()

            # assign the payment to the order
            order_item = OrderItem.objects.all()
            order_item.update(ordered=True)
            for item in order_item:
                item.save()

            order.ordered = True
            order.payment = payment
            order.ref_code = create_ref_code()
            order.save()

            messages.success(self.request, 'Your order was successful!')
            return redirect('/')

        except stripe.error.CardError as e:
            # Since it's a decline, stripe.error.CardError will be caught
            body = e.json_body
            err = body.get('error', {})
            messages.error(self.request, f"{err.get('message')}")
            return redirect('/')

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.error(self.request, 'Rate limit error')
            return redirect('/')

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.error(self.request, 'Invalid prameters')
            return redirect('/')

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.error(self.request, 'Not authenticated')
            return redirect('/')

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.error(self.request, 'Network error')
            return redirect('/')

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.error(
                self.request, 'Something went wrong. You were not charged. Please try again.')
            return redirect('/')

        except Exception as e:
            # Send an email to ourselves
            messages.error(
                self.request, 'A serious error occurred. We have been notifed.')
            return redirect('/')
