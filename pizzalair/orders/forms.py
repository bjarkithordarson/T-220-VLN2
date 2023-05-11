from django.forms import ModelForm
from .models import Order


class BillingForm(ModelForm):
    class Meta:
        model = Order
        fields = ['billing_name', 'billing_address', 'billing_city', 'billing_postal_code', 'billing_country']

class PaymentMethodForm(ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']

class CardPaymentForm(ModelForm):
    class Meta:
        model = Order
        fields = ['payment_card_name', 'payment_card_number', 'payment_expiry_month', 'payment_expiry_year', 'payment_cvc']
