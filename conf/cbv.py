from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from accounts.models import Profile


def is_check_writer(user):
    """Writer 권한 체크"""
    return user.is_authenticated and len(
        Profile.objects.filter(user_id=user.id, is_writer=True)) == 1


@method_decorator(user_passes_test(is_check_writer), name='dispatch')
class WriterCreateView(CreateView):
    """Writer 권한 체크하는 CreateView"""

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

@method_decorator(user_passes_test(is_check_writer), name='dispatch')
class WriterUpdateView(UpdateView):
    """Writer 권한 체크하는 UpdateView"""

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user_id == request.user.id:
            return super().get(request, *args, **kwargs)
        else:
            messages.warning(request, '수정 권한이 없습니다.')
            return redirect(obj.get_absolute_url())

    def post(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user_id == request.user.id:
            return super().post(request, *args, **kwargs)
        else:
            messages.warning(request, '수정 권한이 없습니다.')
            return redirect(obj.get_absolute_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
