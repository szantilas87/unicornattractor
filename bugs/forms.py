from django import forms

class FilterView(forms.Form):
    ORDER_BY_CHOICES = [
        ('name_az', 'Name: A - Z'),
        ('name_za', 'Name: Z - A'),
        ('status_az', 'Status: A - Z'),
        ('status_za', 'Status: Z - A')
    ]
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES, label='')