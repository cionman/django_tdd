from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from til.forms import TilForm
from til.models import Til


@login_required
def til(request):
    if request.method == 'POST':
        form = TilForm(request.POST)
        if form.is_valid():
            til = Til(
                user_id=request.user.id
                , user_name=request.user.username
                , user_email=request.user.email
                , **form.cleaned_data)
            til.save()
            return redirect('til:til')
    else:
        form = TilForm()
    return render(request, 'til/til.html', {
        'form': form
        , 'now': date.today()
        , 'til_list': Til.objects.filter(user_id=request.user.id)
    })
