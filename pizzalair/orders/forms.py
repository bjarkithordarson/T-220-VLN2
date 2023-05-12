from django import forms
from .models import Order


class BillingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['billing_name', 'billing_phone_number', 'billing_address', 'billing_city', 'billing_postal_code', 'billing_country']

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']

class CardPaymentForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_card_name', 'payment_card_number', 'payment_expiry_month', 'payment_expiry_year', 'payment_cvc']
        widgets = {
            'payment_card_number': forms.TextInput(attrs={'placeholder': '1234567890123456'}),
            'payment_expiry_month': forms.TextInput(attrs={'placeholder': '01'}),
            'payment_expiry_year': forms.TextInput(attrs={'placeholder': '2020'}),
            'payment_cvc': forms.TextInput(attrs={'placeholder': '123'}),
        }
