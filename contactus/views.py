from django.shortcuts import render, redirect
from .models import ContactUsInformation, ContactUs
from django.views.generic import View
from django.contrib import messages
from .forms import ContactUsForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

class ContactUs(View):
    def get(self, *args, **kwargs):
        contactus_info = ContactUsInformation.objects.all()[:1]
        form = ContactUsForm()

        context = {
            'contactus_info':contactus_info ,
            'form':form ,
        }
        return render(self.request, 'contact.html', context)
    
    def post(self, *args, **kwargs):
        try:
            form = ContactUsForm(self.request.POST)
            if form.is_valid():
                # name = form.cleaned_data.get('name')
                # email = form.cleaned_data.get('email')
                # subject = form.cleaned_data.get('subject')
                # message = form.cleaned_data.get('message')

                contact = form.save(commit=False)
                contact.save()

                # contact_us.save()
                messages.success(self.request, "done!")
                return redirect("/")
            else:
                messages.info(
                    self.request, "Please fill in the required fields")
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("orders:order_summary")
