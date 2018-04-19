from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login as auth_login

from accounts.models import Profile


def login(request):
    providers = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id,
                                                        sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    return auth_login(request,
                      authentication_form=AuthenticationForm,
                      template_name='accounts/login.html',
                      extra_context={'providers': providers})


class AccountAdapter(DefaultSocialAccountAdapter):

    def new_user(self, request, sociallogin):
        return super().new_user(request, sociallogin)

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        Profile(user=user).save()
        return user

    def populate_user(self, request, sociallogin, data):
        return super().populate_user(request, sociallogin, data)


