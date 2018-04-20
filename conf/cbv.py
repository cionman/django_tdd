from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from accounts.models import Profile


def is_check_writer(user):
    return user.is_authenticated and len(
        Profile.objects.filter(user_id=user.id, is_writer=True)) == 1


@method_decorator(user_passes_test(is_check_writer), name='dispatch')
class WriterCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy() # immutable 해제
        request.POST['user_id'] = request.user.id
        request.POST['user_name'] = request.user.username
        request.POST['user_email'] = request.user.email
        return super().post(request, *args, **kwargs)


@method_decorator(user_passes_test(is_check_writer), name='dispatch')
class WriterUpdateView(UpdateView):
    pass