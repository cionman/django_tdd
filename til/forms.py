from django import forms

from til.models import Til


class TilForm(forms.ModelForm):
    class Meta:
        model = Til
        fields = ['date', 'contents']