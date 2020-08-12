from django import forms


class CityForm(forms.Form):
    city_name = forms.CharField()
