from django.forms import ModelForm
from .models import OfferInstance


class OfferInstanceForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(OfferInstanceForm, self).__init__(*args, **kwargs)
    class Meta:
        model = OfferInstance
        fields = ['offer', 'quantity']
