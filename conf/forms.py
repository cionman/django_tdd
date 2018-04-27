from django import forms
from django.forms import ImageField
from django.template.defaultfilters import filesizeformat

from conf.settings.base import MAX_UPLOAD_SIZE


class RestrictImageFileForm(forms.ModelForm):
    """Image 파일 업로드 제한 Form"""

    def check_image(self, key):
        content = self.cleaned_data.get(key, None)
        if content is not None and content.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                ('최대 파일사이즈는 %s 입니다. 현재 파일사이즈는 %s 입니다.') % (
                    filesizeformat(MAX_UPLOAD_SIZE),
                    filesizeformat(content._size)))
        return content

    def clean(self):
        for key, field in self.fields.items():
            if isinstance(field, ImageField):
                self.check_image(key)
        return super().clean()


class DefaultSetUserForm(forms.ModelForm):
    """기본 유저 정보 Form"""

    class Meta:
        fields = ['user_id', 'user_name', 'user_email']
        widgets = {
            'user_id': forms.HiddenInput,
            'user_name': forms.HiddenInput,
            'user_email': forms.HiddenInput,
        }

    def __init__(self, *args, **kwargs):
        super(DefaultSetUserForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].required = False
        self.fields['user_name'].required = False
        self.fields['user_email'].required = False

