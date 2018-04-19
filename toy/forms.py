from django import forms

from conf.forms import RestrictImageFileForm
from toy.models import Toy


class ToyForm(RestrictImageFileForm):
    class Meta:
        model = Toy
        fields = ['title','url','desc','toy_image', 'tech_stack', 'start_date', 'end_date']


