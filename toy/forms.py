from django import forms

from toy.models import Toy


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['title','url','desc','toy_image', 'tech_stack', 'start_date', 'end_date']


