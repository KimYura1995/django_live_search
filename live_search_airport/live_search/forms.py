from django import forms

from live_search.models import Airport


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ('city',)
