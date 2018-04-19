from django import forms

from codelab.models import CodelabDetail, Codelab
from conf.forms import RestrictImageFileForm


class CodelabForm(RestrictImageFileForm):
    class Meta:
        model = Codelab
        fields = ['title', 'image', 'desc', 'isview']


class CodelabDetailForm(forms.ModelForm):
    class Meta:
        model = CodelabDetail
        fields = ['codelab','title', 'contents', 'slug']
