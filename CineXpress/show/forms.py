from django import forms
from . import models

class ShowForm(forms.ModelForm):
    show_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        ),
        label="Show Date"
    )

    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}
        ),
        label="Start Time"
    )

    price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter ticket price'}
        ),
        max_digits=6,
        decimal_places=2,
        label="Price (₹)"
    )

    class Meta:
        model = models.Show
        fields = ['movie', 'screen', 'show_date', 'start_time', 'price']
        widgets = {
            'movie': forms.Select(attrs={'class': 'form-control'}),
            'screen': forms.Select(attrs={'class': 'form-control'}),
        }
