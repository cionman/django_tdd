from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from accounts.models import Profile


def is_check_writer(user):
    return user.is_authenticated and len(
        Profile.objects.filter(user_id=user.id, is_writer=True)) == 1


@method_decorator(user_passes_test(is_check_writer), name='dispatch')
class WriterCreateView(CreateView):
    pass


@method_decorator(user_passes_test(is_check_writer), name='dispatch')
class WriterUpdateView(UpdateView):
    pass
