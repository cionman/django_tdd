from django import forms

from codelab.models import CodelabDetail, Codelab
from conf.forms import RestrictImageFileForm, DefaultSetUserForm
from conf.widgets import SingleToastUIEditorWidget


class CodelabForm(RestrictImageFileForm, DefaultSetUserForm):
    class Meta(DefaultSetUserForm.Meta):
        model = Codelab
        fields = ['title', 'image', 'desc', 'isview', 'category'] + DefaultSetUserForm.Meta.fields


class CodelabDetailForm(DefaultSetUserForm):
    class Meta(DefaultSetUserForm.Meta):
        model = CodelabDetail
        fields = ['codelab','title', 'contents', 'slug'] + DefaultSetUserForm.Meta.fields
        widgets = {
            'contents' : SingleToastUIEditorWidget,
            'user_id': forms.HiddenInput,
            'user_name': forms.HiddenInput,
            'user_email': forms.HiddenInput,
        }
