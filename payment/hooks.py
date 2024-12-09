from datetime import time
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
from .models import Order

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    time.sleep(5)
    # Grab the info that paypal sends
    paypal_obj = sender
    # Grab the Invoice
    my_Invoice = str(paypal_obj.invoice)

    my_Order = Order.objects.get(invoice=my_Invoice)
    my_Order.paid = True
    my_Order.save()


    #print(paypal_obj)
    #print(f'Amount Paid: {paypal_obj.mc_gross}')