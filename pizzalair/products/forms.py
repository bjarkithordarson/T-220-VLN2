from django import forms
from .models import OfferInstance, Offer, OfferTemplate


class OfferInstanceForm(forms.ModelForm):

    def __init__(self, offer_id, *args, **kwargs):
        super(OfferInstanceForm, self).__init__(*args, **kwargs)

        offer = Offer.objects.filter(id=self.fields['offer'].initial).first()
        self.fields['offer'].initial = offer_id
        self.fields['quantity'].initial = 1

        templates = OfferTemplate.objects.filter(offer=offer_id)
        print("TEMPLATES")
        print(templates)
        for template in templates:
            products = template.category.products.all()
            print("Qty: " + str(template.quantity))
            for i in range(template.quantity):
                print(f"products_{i}")
                field = forms.ModelChoiceField(queryset=products)
                field.label = template.category.name + " " + str(i+1)
                self.fields[f"products_{template.id}_{i}"] = field

    def clean(self):
        products = []
        offer = Offer.objects.filter(id=self.cleaned_data['offer'].id).first()
        templates = OfferTemplate.objects.filter(offer=offer.id)
        for template in templates:
            for i in range(template.quantity):
                products.append(self.cleaned_data[f"products_{template.id}_{i}"])

        self.cleaned_data['products'] = products

    def save(self, commit=True):
        instance = super(OfferInstanceForm, self).save(commit=False)
        instance.save()
        print("==============================")
        print(self.cleaned_data['products'])

        for product in self.cleaned_data['products']:
            instance.products.add(product)

        if commit:
            instance.save()

        return instance

    class Meta:
        model = OfferInstance
        fields = ['offer', 'quantity']
        widgets = {
            'offer': forms.HiddenInput()
        }
