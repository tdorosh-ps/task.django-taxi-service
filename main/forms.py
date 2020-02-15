from django import forms
from main.models import Order

class OrderForm(forms.ModelForm):
    desired_time = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M'], help_text="In format: дд.мм.рррр гг:хх")
    class Meta:
        model = Order
        fields = ('client', 'telephone', 'order_adress', 'destination_adress', 'desired_time')
        help_texts = {
            'client': 'Only cyrillic alphabet: from 3 to 50 characters',
            'telephone': 'In format: +380(ХХ)ХХХ-ХХ-ХХ',
            'order_adress': '100 characters max',
            'destination_adress': '100 characters max'
        }