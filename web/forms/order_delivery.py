from django import forms


class OrderDelivery(forms.Form):
    delivery_method = forms.IntegerField()
    payment_method = forms.IntegerField()
