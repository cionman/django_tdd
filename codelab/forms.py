from django import forms

from codelab.models import CodelabDetail, Codelab
from conf.forms import RestrictImageFileForm, DefaultSetUserForm


class CodelabForm(RestrictImageFileForm, DefaultSetUserForm):
    class Meta(DefaultSetUserForm.Meta):
        model = Codelab
        fields = ['title', 'image', 'desc', 'isview'] + DefaultSetUserForm.Meta.fields


class CodelabDetailForm(DefaultSetUserForm):
    class Meta(DefaultSetUserForm.Meta):
        model = CodelabDetail
        fields = ['codelab','title', 'contents', 'slug'] + DefaultSetUserForm.Meta.fields
