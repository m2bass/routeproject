from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['route_id', 'agency_id', 'route_short_name', 'route_long_name', 'route_type']
