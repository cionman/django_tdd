from django import forms

from codelab.models import CodelabDetail, Codelab
from conf.forms import RestrictImageFileForm, DefaultSetUserForm
from conf.widgets import SingleToastUIEditorWidget


class CodelabForm(RestrictImageFileForm, DefaultSetUserForm):
    class Meta:
        model = Codelab
        fields = ['title', 'image', 'desc', 'isview', 'category']


class CodelabDetailForm(DefaultSetUserForm):
    class Meta:
        model = CodelabDetail
        fields = ['codelab','title', 'contents','contents_markdown', 'slug']
        widgets = {
            'contents' : SingleToastUIEditorWidget,
            'contents_markdown' : forms.HiddenInput,
        }
