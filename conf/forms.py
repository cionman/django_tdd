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

    def __init__(self, user, *args, **kwargs):
        super(DefaultSetUserForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        self.instance.user_id = self.user.id
        self.instance.user_name = self.user.username
        self.instance.user_email = self.user.email
        return super().save(commit)
